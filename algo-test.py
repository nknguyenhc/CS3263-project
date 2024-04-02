from utils.xiangqi import Xiangqi
from utils.basealgo import BaseAlgo
from movepickalgo import MovepickAlgo
from evaluationalgo import EvaluationAlgo
from PValgo import PVAlgo
from main import read_board
import sys

# algo playing as red
algo1: BaseAlgo = PVAlgo()
# algo playing as black
algo2: BaseAlgo = PVAlgo()

def main():
    if len(sys.argv) > 1:
        board = read_board(sys.argv[1])
    else:
        board = Xiangqi()
    
    for i in range(200):
        if i % 10 == 0:
            print(board)
            print()
        if board.turn:
            move = algo1.next_move(board)
            print(f"R: {move.to_notation(board)}")
        else:
            move = algo2.next_move(board)
            print(f"B: {move.to_notation(board)}")
        board = board.move(move)
        if len(board.actions()) == 0:
            break
    
    print("Final board:")
    print(board)
    if len(board.actions()) != 0:
        print("Draw!")
    elif board.turn:
        print("Black wins!")
    else:
        print("Red wins!")


if __name__ == '__main__':
    main()
