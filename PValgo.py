from enum import Enum
from math import inf
from time import time


from transpositiontable import BoundType, TTEntry, TranspositionTable
from utils.basealgo import BaseAlgo
from utils.xiangqi import Move, Xiangqi, MoveMode
from evaluation import Evaluation
from movepicker import MovePicker

class SearchTimeout(Exception):
    pass

class NodeType(Enum):
    NONE = -1
    ROOT = 0
    PV = 1
    NON_PV = 2

class PVSeqNode:

    def __init__(self, move: Move | None, next = None):
        self.move = move
        self.next = next

    def to_list(self):
        seq = []
        cur = self
        while cur:
            seq.append(cur.move)
            cur = cur.next
        return seq

    def __str__(self):
        return self.to_list().__str__()

class SearchInfo:

    def __init__(self):
        self.start_time = time()
        self.depth = 0
        self.ply = 0
        self.root_pv: Move | None = None
        self.optimal_seq: list[PVSeqNode | None]

def prioritize_tt_move(generated_moves, tt_move):
    if tt_move is None:
        return
    for i, move in enumerate(generated_moves):
        if move == tt_move:
            # a simple swap!
            generated_moves[0], generated_moves[i] = tt_move, generated_moves[0]
            return
    # assert False, f"there is no {tt_move} in {generated_moves}"

class PVAlgo(BaseAlgo):

    def __init__(self):
        self.evaluation = Evaluation()
        self.movepicker = MovePicker()
        self.transposition_table_q = TranspositionTable()
        self.transposition_table_p = TranspositionTable()

    def quiescence(self, xiangqi: Xiangqi, alpha: int, beta: int, depth: int = 5,
                   node_type: NodeType = NodeType.NONE):
        info = self.info

        if depth == 0:
            return self.evaluation.evaluate(xiangqi)

        tt_entry: TTEntry = self.transposition_table_q.lookup(xiangqi)
        if tt_entry:
            tt_score = tt_entry.score
            tt_bound = tt_entry.bound
            tt_depth = tt_entry.depth
            if (tt_depth >= depth
                and (tt_bound == BoundType.EXACT or
                (tt_bound == BoundType.UPPER and tt_score <= alpha) or
                (tt_bound == BoundType.LOWER and tt_score >= beta))):
                # print(f"tt_table hit at {depth=} with {tt_score=}")
                return tt_score
            tt_move = tt_entry.move
        else:
            tt_move = None

        score = self.evaluation.evaluate(xiangqi)
        if score >= beta:
            # score is out of bound, we create a new entry in the transposition table
            # signal that the actual valuation of this node is bigger than beta but
            # there is no need for us to actually search here to find out the actual value
            tt_entry = TTEntry(xiangqi, depth, BoundType.LOWER, score, None)
            self.transposition_table_q.update(tt_entry)
            return beta

        if score > alpha:
            # we know that the score lies between alpha and beta, so in this case
            # we know that this score the EXACT score
            alpha = score
            tt_bound = BoundType.EXACT
        else:
            # otherwise, the actual score of this node is bounded by alpha. We don't know
            # what is the actual value, we only know the bound!
            tt_bound = BoundType.UPPER

        # line 1348: tt_eval can be used as a better evaluation

        best_score = score
        best_move: Move | None = None
        next_depth = depth - 1

        generated_moves = self.movepicker.move_order(xiangqi, mode=MoveMode.CAPTURE | MoveMode.CHECK)
        prioritize_tt_move(generated_moves, tt_move)
        for move in generated_moves:
            next_xiangqi = xiangqi.move(move, in_place=False)
            info.ply += 1
            score = -self.quiescence(next_xiangqi, -beta, -alpha, next_depth)
            info.ply -= 1

            if score > best_score:
                # we found a better move!
                best_score = score
                best_move = move

            if score >= beta:
                # there is no need to continue. The actual value will be bigger than beta
                # is this correct though?
                tt_entry = TTEntry(xiangqi, depth, BoundType.LOWER, beta, best_move)
                self.transposition_table_q.update(tt_entry)
                return beta

            if score > alpha:
                alpha = score
                tt_bound = BoundType.EXACT
        tt_entry = TTEntry(xiangqi, depth, tt_bound, alpha, best_move)
        self.transposition_table_q.update(tt_entry)
        return alpha

    def principal_variation(self, xiangqi: Xiangqi, alpha: int, beta: int, depth: int,
                            node_type: NodeType = NodeType.NONE):
        init_depth = depth
        info = self.info
        is_root = node_type == NodeType.ROOT
        pv_node = node_type != NodeType.NON_PV

        if depth <= 0:
            return self.quiescence(xiangqi, alpha, beta, 5,
                                   NodeType.PV if pv_node else NodeType.NON_PV)

        tt_entry: TTEntry = self.transposition_table_p.lookup(xiangqi)
        tt_score = tt_entry and tt_entry.score
        tt_bound = tt_entry and tt_entry.bound
        tt_depth = tt_entry and tt_entry.depth
        tt_move = tt_entry and tt_entry.move
        tt_capture = tt_move and tt_move._is_capture(xiangqi)

        # at non-PV nodes we check for an early TT cutoff
        if (not pv_node
            and tt_depth is not None
            and tt_depth >= depth
            and (
                (tt_bound == BoundType.EXACT)
                or (tt_bound == BoundType.UPPER and tt_score <= alpha)
                or (tt_bound == BoundType.LOWER and tt_score >= beta)
            )):
            return tt_score

        # static evaluation of the position
        if tt_bound == BoundType.EXACT:
            static_eval = tt_score
        else:
            static_eval = self.evaluation.evaluate(xiangqi)

        if (tt_score is not None
            and (
                (tt_bound == BoundType.UPPER and tt_score <= static_eval) or
                (tt_bound == BoundType.LOWER and tt_score >= static_eval)
            )):
            static_eval = tt_score

        # futility pruning
        if (not pv_node
            and depth < 3 # TODO: tune this
            and static_eval >= beta
            and (not tt_move or tt_capture)):
            return static_eval

        if not is_root and not tt_move:
            depth -= 2 # TODO: tune this

        # only pv_node can cause depth <= at this location
        if depth <= 0:
            return self.quiescence(xiangqi, alpha, beta, 5, NodeType.PV)

        best_move: Move | None = None
        best_score = -inf
        best_seq = None

        # are we on the principal variation right now?
        # if so, we will conduct a null-window search to verify that we are indeed on
        # the principal variation
        is_pvs = False
        tt_bound = BoundType.UPPER
        move_count = 0

        moves = self.movepicker.move_order(xiangqi, mode=MoveMode.ALL)
        prioritize_tt_move(moves, tt_move)

        for move in moves:
            move_count += 1
            info.ply += 1
            is_capture = move._is_capture(xiangqi)
            is_check = move._is_check(xiangqi)
            next_xiangqi = xiangqi.move(move, in_place=False)
            next_depth = depth - 1

            # late move reduction
            if (not pv_node
                and depth >= 2
                and move_count >= 2
                and not is_capture
                and not is_check):
                next_depth -= 1

            if is_pvs:
                score = -self.principal_variation(next_xiangqi, -alpha - 1, -alpha,
                                                  next_depth, NodeType.NON_PV)
                do_full_search = alpha < score < beta
            else:
                do_full_search = True

            if do_full_search:
                score = -self.principal_variation(next_xiangqi, -beta, -alpha,
                                                  next_depth, NodeType.PV)

            info.ply -= 1

            if score > best_score:
                best_score = score
                best_move = move
                best_seq = info.optimal_seq[max(next_depth, 0)]

            if score >= beta:
                tt_entry = TTEntry(xiangqi, depth, BoundType.LOWER, beta, best_move)
                self.transposition_table_p.update(tt_entry)
                return beta

            if score > alpha:
                alpha = score
                tt_bound = BoundType.EXACT
                is_pvs = True

        if is_root:
            info.root_pv = best_move

        tt_entry = TTEntry(xiangqi, depth, tt_bound, alpha, best_move)
        self.transposition_table_p.update(tt_entry)
        info.optimal_seq[init_depth] = PVSeqNode(best_move, best_seq)
        return alpha

    def iterative_deepening(self, xiangqi: Xiangqi, max_depth=5):
        info = self.info
        alpha = -inf
        beta = inf
        for depth in range(1, max_depth + 1):
            info.depth = depth
            info.optimal_seq = [None for _ in range(depth + 1)]
            value = self.principal_variation(xiangqi, alpha, beta, depth, NodeType.ROOT)
            print(f"optimal seq at {depth=}: {info.optimal_seq[depth].to_list()}")
            print(f"valuation at {depth=}: {value}")
        # print(f"{info.evaluations=}")

    def next_move(self, xiangqi: Xiangqi) -> Move | None:
        self.info = SearchInfo()
        try:
            self.iterative_deepening(xiangqi)
        except SearchTimeout:
            pass
        best_move = self.info.root_pv
        return best_move
