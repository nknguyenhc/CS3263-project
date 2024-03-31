from evaluation import Evaluation
from utils.xiangqi import Xiangqi

def test_evaluate():
    board = Xiangqi()
    evaluator = Evaluation()
    initial_advantage = evaluator.evaluate(board)
    assert initial_advantage < 51 and initial_advantage > 49 # advantage due to red moving first

def test_board(filename, expected_value):
    with open(f"sample-boards/{filename}.in", 'r') as f:
        board_string = f.read()
    board = Xiangqi.from_string(board_string)
    print(f"Evaluating {filename}")
    evaluator = Evaluation()
    result = evaluator.evaluate(board)
    print(f"Result: {result}, expected value: {expected_value}")

def main():
    test_evaluate()
    test_board("zhongpao-pingfenma-C89", 60)
    test_board("paobehindpawn", 0)
    test_board("elephant-cannon-advisor-hand", 10)
    test_board("cannons-block-rooks", 160)
    test_board("empty-cannons", 1400)
    test_board("wocaoma", 900)
    test_board("R14-sacrifice-rook", 700)
    test_board("pinned-wocaoma", 0)
    test_board("empty-cannon-vs-pinned-wocaoma", -400)
    test_board("C8+7", -100)

if __name__ == '__main__':
    main()
