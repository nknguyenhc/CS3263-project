from math import inf
from time import time
from transpositiontable import BoundType, TTEntry, TranspositionTable
from utils.basealgo import BaseAlgo
from utils.xiangqi import Move, Xiangqi, MoveMode
from evaluation import Evaluation
from movepicker import MovePicker

class SearchTimeout(Exception):
        pass

class SearchInfo:

    def __init__(self):
        self.start_time = time()
        self.depth = 0
        self.ply = 0
        self.best_action: Move | None = None
        self.root_pv: Move | None = None
        self.optimal_path: list[Move]
        self.evaluations: list[tuple[float, Xiangqi]]

def prioritize_tt_move(generated_moves, tt_move):
    if tt_move is None:
        return
    for i, move in enumerate(generated_moves):
        if move == tt_move:
            # a simple swap!
            generated_moves[0], generated_moves[i] = tt_move, generated_moves[0]
            return
    assert False, f"there is no ${tt_move} in ${generated_moves}"

class PVAlgo(BaseAlgo):

    def __init__(self):
        self.evaluation = Evaluation()
        self.movepicker = MovePicker()
        self.transposition_table = TranspositionTable()

    def quiescence(self, xiangqi: Xiangqi, alpha: int, beta: int, depth: int = 5):
        info = self.info

        if depth == 0:
            return self.evaluation.evaluate(xiangqi)

        tt_entry: TTEntry = self.transposition_table.lookup(xiangqi)
        if tt_entry:
            tt_score = tt_entry.score
            tt_bound = tt_entry.bound
            tt_depth = tt_entry.depth
            if (tt_depth >= depth 
                and (tt_bound == BoundType.BOUND_EXACT or 
                (tt_bound == BoundType.BOUND_UPPER and tt_score <= alpha) or 
                (tt_bound == BoundType.BOUND_LOWER and tt_score >= beta))):
                return tt_score
            tt_move = tt_entry.move
        else:
            tt_move = None
        
        score = self.evaluation.evaluate(xiangqi)        
        if score >= beta:
            # score is out of bound, we create a new entry in the transposition table
            # signal that the actual valuation of this node is bigger than beta but 
            # there is no need for us to actually search here to find out the actual value
            tt_entry = TTEntry(xiangqi, depth, BoundType.BOUND_LOWER, score, None)
            self.transposition_table.update(tt_entry)
            return beta

        if score > alpha:
            # we know that the score lies between alpha and beta, so in this case
            # we know that this score the EXACT score
            alpha = score
            tt_bound = BoundType.BOUND_EXACT
        else:
            # otherwise, the actual score of this node is bounded by alpha. We don't know
            # what is the actual value, we only know the bound!
            tt_bound = BoundType.BOUND_UPPER

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
                tt_entry = TTEntry(xiangqi, depth, BoundType.BOUND_LOWER, beta, best_move)
                self.transposition_table.update(tt_entry)
                return beta

            if score > alpha:
                alpha = score
                # we now know the exact value of this node!
                tt_bound = BoundType.BOUND_EXACT
                
        # at the end of the function, we need to updte the transposition table
        # note that alpha is also the current "known" value of this node. Not score!
        tt_entry = TTEntry(xiangqi, depth, tt_bound, alpha, best_move)
        self.transposition_table.update(tt_entry)
        return alpha

    def principal_variation(self, xiangqi: Xiangqi, alpha: int, beta: int, depth: int):
        info = self.info
        is_root = info.ply == 0

        if depth == 0:
            return self.quiescence(xiangqi, alpha, beta)

        # TODO: TT lookup here

        # best_score that we can achieve at this state
        best_score = -inf

        # best_action (move) at this state
        # TODO: (optional) store k best moves in a list, instead of storing a single move
        best_action: Move | None = None

        # are we on the principal variation right now?
        # if so, we will conduct a null-window search to verify that we are indeed on
        # the principal variation
        is_pvs = False
        next_depth = depth - 1

        moves = self.movepicker.move_order(xiangqi, mode=MoveMode.ALL)
        for action in moves:
            next_xiangqi = xiangqi.move(action, in_place=False)
            info.ply += 1

            do_search = True
            if is_pvs:
                # null window search, on principal variation
                score = -self.principal_variation(next_xiangqi, -alpha - 1, -alpha, next_depth)
                do_search = alpha < score < beta

            if do_search:
                score = -self.principal_variation(next_xiangqi, -beta, -alpha, next_depth)

            # reset the search information
            info.ply -= 1

            if score > best_score:
                best_score = score
                best_action = action

            # update the bounds (alpha and beta)
            if score >= beta:
                # tt_entry = TTEntry(depth, BOUND_LOWER, beta, best_action)
                # put_tt_entry(tt_key, tt_entry)
                return beta

            if score > alpha:
                alpha = score
                is_pvs = True
                if is_root:
                    info.root_pv = action
                    info.evaluations.append((score, xiangqi))

        # TODO: update TT
        # return the best score so far, (its alpha if out of the loop)
        info.optimal_path[depth] = best_action.to_notation(xiangqi)
        return alpha


    def iterative_deepening(self, xiangqi: Xiangqi, max_depth=4):
        info = self.info
        # TODO: use specific inf value
        alpha = -inf
        beta = inf
        for depth in range(1, max_depth):
            info.depth = depth
            info.optimal_path = [None for _ in range(depth + 1)]
            info.evaluations = []
            value = self.principal_variation(xiangqi, alpha, beta, depth)
            # policy
            info.best_action = info.root_pv
        print(f"{info.evaluations=}")
        # TODO
        print(f"{info.optimal_path=}")
        
        

    def next_move(self, xiangqi: Xiangqi) -> Move | None:
        self.info = SearchInfo()
        try:
            self.iterative_deepening(xiangqi)
        except SearchTimeout:
            pass
        best_action = self.info.best_action
        return best_action
