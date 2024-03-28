from movepicker import MovePicker
from utils.xiangqi import Xiangqi, MoveMode

def test_board(filename):
    with open(f"sample-boards/{filename}.in", 'r') as f:
        board_string = f.read()
    board = Xiangqi.from_string(board_string)
    print(f"Picking moves in {filename}")
    move_picker = MovePicker()
    moves = [move.to_notation(board) for move in move_picker.move_order(board, MoveMode.ALL)]
    print(f"Result: {moves}")

def main():
    test_board("cannons-block-rooks")
    test_board("elephant-cannon-advisor-hand")
    test_board("empty-cannon-vs-pinned-wocaoma")
    test_board("empty-cannons")
    test_board("paobehindpawn")
    test_board("pinned-wocaoma")
    test_board("R14-sacrifice-rook")
    test_board("wocaoma")
    test_board("zhongpao-pingfenma-C89")

if __name__ == '__main__':
    main()
