from collections import OrderedDict

from utils.xiangqi import Xiangqi

class TTEntry:

    def __init__(self, key: Xiangqi, depth, bound, score, move):
        self.key = key
        self.depth = depth
        self.bound = bound
        self.score = score
        self.move = move

class TranspositionTable:

    def __init__(self, maxsize=1024):
        self.table = OrderedDict()
        self.maxsize = 1024

    def probe(self, key):
        # probe for an tt entry in the table
        entry = self.table.get(key, None)
        if entry is not None:
            self.table.move_to_end(key, last=True)
        return entry

    def update(self, entry):
        self.table[entry.key] = entry
        if len(self.table) > self.mazsize:
            self.table.popitem(last=False)
