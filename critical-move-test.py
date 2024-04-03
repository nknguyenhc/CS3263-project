"""Tests if at critical junction, the algo is able to produce the only correct move.
"""

from utils.xiangqi import Xiangqi
from PValgo import PVAlgo

algo = PVAlgo()

def test_board(board_name, expected_move):
    with open(f"critical-moves/{board_name}.in", 'r') as f:
        board_string = f.read()
    
    print(f"Testing {board_name}")
    board = Xiangqi.from_string(board_string)
    move = algo.next_move(board).to_notation(board)
    if move != expected_move:
        print("Result: FAILED!")
        print(f"Expected move: {expected_move}, Algo choose: {move}")
    else:
        print("Result: PASSED!")

def main():
    test_board("take-back-rook", "H7-8")
    test_board("run-horse", "H3-5")
    test_board("must-use-advisor", "A5-4")

if __name__ == '__main__':
    main()
