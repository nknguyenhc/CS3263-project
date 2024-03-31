from utils.basealgo import BaseAlgo
from utils.xiangqi import Move, Xiangqi, MoveMode
from movepicker import MovePicker

class MovepickAlgo(BaseAlgo):
    def __init__(self):
        self.movepicker = MovePicker()

    def next_move(self, xiangqi: Xiangqi) -> Move | None:
        moves = self.movepicker.move_order(xiangqi, MoveMode.ALL)
        return moves[0] if len(moves) > 0 else None
