from utils.xiangqi import Xiangqi
from randomalgo import RandomAlgo

# Replace this line with your algo
algo = RandomAlgo()

def test_puzzle(puzzle_name, move_limit, expected_moves):
    """Tests a puzzle, a definite sequence of checks/kills to checkmate.
    """
    print(f"Testing puzzle {puzzle_name}")
    with open(f"puzzles/{puzzle_name}.in", 'r') as f:
        board_string = f.read()
    
    board = Xiangqi.from_string(board_string)
    moves = []
    for _ in range(2 * move_limit):
        move = algo.next_move(board)
        if move is None:
            break
        moves.append(move.to_notation(board))
        board = board.move(move)
    
    print(f"Result: {moves}")
    print(f"Expected: {expected_moves}")

    actions = board.actions()
    if len(actions) == 0 and not board.turn and len(moves) >= len(expected_moves):
        print("Puzzle SOLVED!")
    else:
        print("Puzzle FAILED!")
    print()

def main():
    test_puzzle("3-move/wocaoma", 5, ["H8+7", "K5.6", "R3.4", "A5+6", "R4+1"])
    test_puzzle("3-move/advisor-hand", 5, ["R6+1", "A5-4", "H8-6", "K5+1", "R7+3"])
    test_puzzle("3-move/double-rooks", 5, ["R6+1", "K5+1", "R3+4", "K5+1", "R6-2"])
    test_puzzle("3-move/rook-double-cannons", 5, ["R2+6", "K6+1", "R2-1", "K6-1", "C3+2"])
    
    print()
    test_puzzle("4-move/cannon-behind-horse", 6, ["R5+3", "K4+1", "R5.6", "K4-1", "C7.6", "A4-5", "H4+6"])
    test_puzzle("4-move/double-cannons", 6, ["R4+5", "K5+1", "R4.5", "K5.4", "C5.6", "A4-5", "C2.6"])
    test_puzzle("4-move/elephant-block-king", 6, ["R7-1", "K4+1", "R7-1", "K4-1", "R7+1", "K4+1", "A5+6"])
    test_puzzle("4-move/wocaoma", 6, ["H2+3", "K5+1", "H3-4", "K5-1", "R2.5", "A4+5", "H4+3"])

    print()
    test_puzzle("6-move/fishing-horse", 7, ["R1+2", "K6+1", "H1+2", "A5+4", "R1.5", "+A-5", "H2+3", "K6+1", "R5.2", "P3.4", "R2-2"])
    test_puzzle("6-move/wocaoma-double-cannons", 7, ["H5+7", "K5.4", "R8.6", "C1.4", "R6+1", "A5+4", "C5.6", "A4-5", "C6-3", "H8+6", "C9.6"])

    print()
    test_puzzle("7-move/fishing-horse", 9, ["R4+7", "K5.6", "R2+3", "E5-7", "R2.3", "K6+1", "H2+3", "K6+1", "R3-2", "K6-1", "R3.2", "K6-1", "R3+2"])
    test_puzzle("7-move/rook-double-cannons", 9, ["C2+3", "K5+1", "R2+5", "K5+1", "C1-2", "A6-5", "R2-1", "A5+6", "R2-1", "K5-1", "R2+2", "K5-1", "C1+2"])
    test_puzzle("7-move/double-rooks-king", 9, ["R5.4", "A5+6", "R4+3", "K6.5", "R7+4", "K5-1", "R7+1", "K5+1", "R7-1", "K5-1", "R4.5", "A4-5", "R7+1"])
    test_puzzle("7-move/advisor-hand-cannon-horse", 9, [
        ["H2+4", "K5.6", "C5.4", "R9.6", "C1+7", "K6+1", "H4+2", "R6.9", "C1-1", "R9-5", "H2-4", "K6+1", "P3.4"],
        ["H2+4", "K5.6", "C5.4", "R9.6", "C1+7", "K6+1", "H4+2", "R6.9", "H2-3", "K6+1", "P3.4", "R9.6", "P4+1"],
    ])

if __name__ == '__main__':
    main()
