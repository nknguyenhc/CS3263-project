from collections import OrderedDict
from enum import Enum

from utils.xiangqi import Xiangqi

class BoundType(Enum):
    NONE = 0
    LOWER = 1
    UPPER = 2
    EXACT = LOWER | UPPER

class TTEntry:

    def __init__(self, key: Xiangqi, depth, bound: BoundType, score, move):
        self.key = key
        self.depth = depth
        self.bound = bound
        self.score = score
        self.move = move

class TranspositionTable:

    def __init__(self, maxsize=32768):
        self.table = OrderedDict()
        self.maxsize = maxsize

    def lookup(self, key):
        entry = self.table.get(key, None)
        if entry is not None:
            self.table.move_to_end(key, last=True)
        return entry

    def pop_front(self):
        for _ in range(self.maxsize // 4):
            self.table.popitem(last=False)

    def update(self, entry):
        self.table[entry.key] = entry
        if len(self.table) > self.maxsize:
            self.pop_front()
