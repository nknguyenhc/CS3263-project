from utils.basealgo import BaseAlgo
from utils.xiangqi import Move, Xiangqi, MoveMode
from evaluation import Evaluation
from movepicker import MovePicker

class EvaluationAlgo(BaseAlgo):
    INF = 30000

    def __init__(self):
        self.evaluator = Evaluation()
        self.movepicker = MovePicker()
    
    def next_move(self, xiangqi: Xiangqi) -> Move | None:
        _, move = self.negamax(xiangqi, 4, -EvaluationAlgo.INF, EvaluationAlgo.INF)
        return move
    
    def negamax(self, xiangqi: Xiangqi, depth: int, alpha: float, beta: float):
        if depth == 0:
            return (1 if xiangqi.turn else -1) * self.evaluator.evaluate(xiangqi), None
        
        value = -EvaluationAlgo.INF
        best_move = None
        for move in self.movepicker.move_order(xiangqi, None, None, None, MoveMode.ALL):
            new_value, _ = self.negamax(xiangqi.move(move), depth - 1, -beta, -alpha)
            new_value = -new_value
            if best_move is None:
                best_move = move
                value = new_value
            if new_value > value:
                value = new_value
                best_move = move
            if value >= beta:
                break
            alpha = max(alpha, value)

        return value, best_move
