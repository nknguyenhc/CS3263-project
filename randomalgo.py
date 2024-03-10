import random
from utils.basealgo import BaseAlgo

class RandomAlgo(BaseAlgo):
    def next_move(self, xiangqi):
        move = random.choice(xiangqi.actions())
        return move
