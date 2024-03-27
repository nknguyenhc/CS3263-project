from math import inf
from time import time
from utils.basealgo import BaseAlgo
from utils.xiangqi import Move, Xiangqi
from evaluation import Evaluation


class SearchTimeout(Exception):
        pass

class SearchInfo:

    def __init__(self):
        self.start_time = time()
        self.depth = 0
        self.ply = 0
        self.best_action: Move | None = None
        self.root_pv: Move | None = None

class PVAlgo(BaseAlgo):

    def __init__(self):
        self.evaluation = Evaluation() # TODO, use dep inject

    def quiescence(self, alpha: int, beta: int, depth=0):
        pass

    def principal_variation(self, xiangqi: Xiangqi, alpha: int, beta: int, depth: int):
        info = self.info
        is_root = info.ply == 0

        if depth == 0:
            return self.evaluation.evaluate(xiangqi)

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

        for action in xiangqi.actions():
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

        # TODO: update TT

        # return the best score so far, (its alpha if out of the loop)
        return alpha


    def iterative_deepening(self, xiangqi: Xiangqi, max_depth=4):
        info = self.info
        # TODO: use specific inf value
        alpha = -inf
        beta = inf
        for depth in range(1, max_depth):
            info.depth = depth
            value = self.principal_variation(xiangqi, alpha, beta, depth)
            info.best_action = info.root_pv

    def next_move(self, xiangqi: Xiangqi) -> Move | None:
        self.info = SearchInfo()
        try:
            self.iterative_deepening(xiangqi)
        except SearchTimeout:
            pass
        best_action = self.info.best_action
        return best_action
