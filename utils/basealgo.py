from utils.xiangqi import Xiangqi, Move

class BaseAlgo:
    def next_move(self, xiangqi: Xiangqi) -> Move | None:
        """Given a board configuration, returns the move that this algorithm decides to take.
        """
        raise NotImplementedError
