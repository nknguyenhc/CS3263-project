from utils.xiangqi import Xiangqi, InvalidMoveException
from randomalgo import RandomAlgo

# Replace this line with your algo
algo = RandomAlgo()

def main():
    print('Welcome! In this programme, you can test out your algorithm by manually playing against it.')
    print('Note that the board will always be displayed with red side at the bottom and black side on top.')
    turn_string = input('Please decide if you want to play as red (go first) or black (go second): (R/B) ')
    while turn_string != 'R' and turn_string != 'B':
        turn_string = input('Invalid, please key in again: (R/B) ')
    
    if turn_string == 'R':
        human_turn, algo_turn = True, False
    else:
        human_turn, algo_turn = False, True

    board = Xiangqi()
    actions = board.actions()
    while len(actions) != 0:
        print('Current board:')
        print(board)
        print()
        if board.turn == algo_turn:
            move = algo.next_move(board)
            print(f'Algo choose: {move}')
        else:
            move_string = input('Please key in your move: ')
            try:
                move = board.parse_move(move_string)
            except InvalidMoveException as e:
                print(e)
                continue
            except Exception as e:
                print(f"Unhandled exception: {e}")
                continue
        board = board.move(move)
        print()
        actions = board.actions()
    
    print('Current board:')
    print(board)
    print()
    if board.turn == algo_turn:
        print("You won!")
    else:
        print("Algo won!")

if __name__ == '__main__':
    main()
