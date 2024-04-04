"""Tests if at critical junction, the algo is able to produce the only correct move.
Also tests if at certain boards, whether the engine will make the same mistake as playtesting discovered.
"""

from utils.xiangqi import Xiangqi
from PValgo import PVAlgo

algo = lambda: PVAlgo()

def test_board(board_name, expected_move):
    with open(f"critical-moves/{board_name}.in", 'r') as f:
        board_string = f.read()
    
    print(f"Testing {board_name}")
    board = Xiangqi.from_string(board_string)
    move = algo().next_move(board).to_notation(board)
    if move != expected_move:
        print("Result: FAILED!")
        print(f"Expected move: {expected_move}, Algo choose: {move}")
    else:
        print("Result: PASSED!")

def test_mistake(board_name, wrong_move):
    with open(f"mistakes/{board_name}.in", 'r') as f:
        board_string = f.read()
    
    print(f"Testing {board_name}")
    board = Xiangqi.from_string(board_string)
    move = algo().next_move(board).to_notation(board)
    if move == wrong_move:
        print(f"Result: FAILED! The engine makes the same mistake of {move}")
    else:
        print(f"Result: PASSED! Move made: {move}")

def main():
    test_board("take-back-rook", "H7-8")
    test_board("run-horse", "H3-5")
    test_board("must-use-advisor", "A5-4")
    test_board("R1.4-protect-lane", "R1.4")
    test_board("R9.6-develop-rook", "R9.6")

    test_mistake("trapped-cannon", "C8-1")
    test_mistake("develop-rook", "R9+2")
    test_mistake("cannon-left-unprotected", "R2.1")

if __name__ == '__main__':
    main()
