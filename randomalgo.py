import random
from utils.basealgo import BaseAlgo

class RandomAlgo(BaseAlgo):
    def next_move(self, xiangqi):
        actions = xiangqi.actions()
        if len(actions) == 0:
            return None
        move = random.choice(actions)
        return move
