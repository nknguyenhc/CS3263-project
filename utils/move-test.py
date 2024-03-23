from xiangqi import Xiangqi, Rook, Horse, Elephant, Advisor, King, Cannon, Pawn, Move

def test_king_move():
    board = Xiangqi(board=[
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    move = board.parse_move('K5.4')
    assert move == Move(King, (9, 4), (9, 5))
    board = board.move(move)
    move = board.parse_move('K4.5')
    assert move == Move(King, (1, 3), (1, 4))
    board = board.move(move)
    move = board.parse_move('K4+1')
    assert move == Move(King, (9, 5), (8, 5))
    board = board.move(move)
    move = board.parse_move('K5-1')
    assert move == Move(King, (1, 4), (0, 4))

def test_advisor_move():
    board = Xiangqi(board=[
        [None, None, None, Advisor(False), None, King(False), None, None, None],
        [None, None, None, None, Advisor(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, Advisor(True), King(True), None, None, None, None],
    ])
    move = board.parse_move('A5+4')
    assert move == Move(Advisor, (8, 4), (7, 5))
    board = board.move(move)
    move = board.parse_move('A5+6')
    assert move == Move(Advisor, (1, 4), (2, 5))
    board = board.move(move)
    move = board.parse_move('A6+5')
    assert move == Move(Advisor, (9, 3), (8, 4))
    board = board.move(move)
    move = board.parse_move('A6-5')
    assert move == Move(Advisor, (2, 5), (1, 4))

def test_elephant_move():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Elephant(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), Elephant(True), None, None],
    ])
    move = board.parse_move('E3+5')
    assert move == Move(Elephant, (9, 6), (7, 4))
    board = board.move(move)
    move = board.parse_move('E7-9')
    assert move == Move(Elephant, (4, 6), (2, 8))
    board = board.move(move)
    move = board.parse_move('E5+7')
    assert move == Move(Elephant, (7, 4), (5, 2))
    board = board.move(move)
    move = board.parse_move('E9-7')
    assert move == Move(Elephant, (2, 8), (0, 6))

def test_horse_move():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, Horse(False), None, None, None],
        [None, None, None, None, None, None, Rook(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Pawn(True), None],
        [None, None, None, None, None, None, None, None, Horse(True)],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    move = board.parse_move('H1+3')
    assert move == Move(Horse, (5, 8), (4, 6))
    board = board.move(move)
    move = board.parse_move('H6+8')
    assert move == Move(Horse, (1, 5), (2, 7))
    board = board.move(move)
    move = board.parse_move('H3+2')
    assert move == Move(Horse, (4, 6), (2, 7))

def test_rook_move():
    board = Xiangqi(board=[
        [None, None, Cannon(False), None, None, None, None, None, None],
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Rook(False), None, None, None, None, None, None, None, None],
        [None, Rook(True), None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    move = board.parse_move('R8.2')
    assert move == Move(Rook, (6, 1), (6, 7))
    board = board.move(move)
    move = board.parse_move('R1+2')
    assert move == Move(Rook, (5, 0), (7, 0))
    board = board.move(move)
    move = board.parse_move('R2+6')
    assert move == Move(Rook, (6, 7), (0, 7))
    board = board.move(move)
    move = board.parse_move('R1-7')
    assert move == Move(Rook, (7, 0), (0, 0))
    board = board.move(move)
    move = board.parse_move('R2.7')
    assert move == Move(Rook, (0, 7), (0, 2))

def test_cannon_move():
    board = Xiangqi(board=[
        [None, None, Elephant(False), None, King(False), None, Elephant(False), None, None],
        [None, None, Cannon(False), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Pawn(True), Cannon(True), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Elephant(True), King(True), None, None, None, None, None],
    ])
    move = board.parse_move('C6.3')
    assert move == Move(Cannon, (6, 3), (6, 6))
    board = board.move(move)
    move = board.parse_move('C3+4')
    assert move == Move(Cannon, (1, 2), (5, 2))
    board = board.move(move)
    move = board.parse_move('C3+6')
    assert move == Move(Cannon, (6, 6), (0, 6))
    board = board.move(move)
    move = board.parse_move('C3+4')
    assert move == Move(Cannon, (5, 2), (9, 2))
    board = board.move(move)
    move = board.parse_move('C3.7')
    assert move == Move(Cannon, (0, 6), (0, 2))
    board = board.move(move)
    move = board.parse_move('C3-9')
    assert move == Move(Cannon, (9, 2), (0, 2))

def test_pawn_move():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Pawn(False), None, None, None, None],
        [None, None, None, None, None, None, Pawn(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    move = board.parse_move('P3+1')
    assert move == Move(Pawn, (6, 6), (5, 6))
    board = board.move(move)
    move = board.parse_move('P5+1')
    assert move == Move(Pawn, (5, 4), (6, 4))
    board = board.move(move)
    move = board.parse_move('P3+1')
    assert move == Move(Pawn, (5, 6), (4, 6))
    board = board.move(move)
    move = board.parse_move('P5.6')
    assert move == Move(Pawn, (6, 4), (6, 5))
    board = board.move(move)
    move = board.parse_move('P3.2')
    assert move == Move(Pawn, (4, 6), (4, 7))

def test_front_back_move():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, Cannon(False), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Cannon(False), None, None, None, None, None, None],
        [Rook(True), None, None, None, None, None, None, None, None],
        [None, None, Pawn(True), None, None, None, None, None, None],
        [Rook(True), None, None, None, None, None, Pawn(False), None, None],
        [None, None, Horse(True), None, None, None, Pawn(False), None, None],
        [None, None, Horse(True), None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    move = board.parse_move('+R+1')
    assert move == Move(Rook, (4, 0), (3, 0))
    board = board.move(move)
    move = board.parse_move('-C+4')
    assert move == Move(Cannon, (1, 2), (5, 2))
    board = board.move(move)
    move = board.parse_move('-R-2')
    assert move == Move(Rook, (6, 0), (8, 0))
    board = board.move(move)
    move = board.parse_move('-C.6')
    assert move == Move(Cannon, (3, 2), (3, 5))
    board = board.move(move)
    move = board.parse_move('-H+5')
    assert move == Move(Horse, (8, 2), (7, 4))
    board = board.move(move)
    move = board.parse_move('+P.6')
    assert move == Move(Pawn, (7, 6), (7, 5))

    board = Xiangqi(board=[
        [None, None, Elephant(False), King(False), None, Advisor(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, Advisor(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Elephant(False), None, None, None, None, None, None],
        [None, None, Elephant(True), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Elephant(True), Advisor(True), None, King(True), None, None, None],
    ])
    move = board.parse_move('+E-5')
    assert move == Move(Elephant, (5, 2), (7, 4))
    board = board.move(move)
    move = board.parse_move('-E+5')
    assert move == Move(Elephant, (0, 2), (2, 4))
    board = board.move(move)
    move = board.parse_move('-A+5')
    assert move == Move(Advisor, (9, 3), (8, 4))
    board = board.move(move)
    move = board.parse_move('+A-5')
    assert move == Move(Advisor, (2, 5), (1, 4))

def test_pawn_order_move():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(True), None, None],
        [None, None, None, None, None, None, Pawn(True), None, None],
        [None, None, Pawn(True), None, None, None, None, None, None],
        [None, None, Pawn(True), None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    move = board.parse_move('13+1')
    assert move == Move(Pawn, (2, 6), (1, 6))
    move = board.parse_move('33+1')
    assert move == Move(Pawn, (6, 6), (5, 6))
    move = board.parse_move('23.4')
    assert move == Move(Pawn, (3, 6), (3, 5))
    move = board.parse_move('17.8')
    assert move == Move(Pawn, (4, 2), (4, 1))

def test_board_str():
    board = Xiangqi()
    assert str(board) == f'R1 H1 E1 A1 K1 A1 E1 H1 R1' \
                      + '\n                          ' \
                      + '\n   C1                C1   ' \
                      + '\nP1    P1    P1    P1    P1' \
                      + '\n                          ' \
                      + '\n                          ' \
                      + '\nP0    P0    P0    P0    P0' \
                      + '\n   C0                C0   ' \
                      + '\n                          ' \
                      + '\nR0 H0 E0 A0 K0 A0 E0 H0 R0' \
                      + '\nturn: 0'

def test_load_board():
    with open('board-test.in') as f:
        board_string = f.read()
        board = Xiangqi.from_string(board_string)
    assert board == Xiangqi(board=[
        [Rook(False), None, Elephant(False), Advisor(False), King(False), Advisor(False), Elephant(False), Rook(False), None],
        [None, None, None, None, None, None, None, None, None],
        [None, Cannon(False), Horse(False), None, None, None, Horse(False), Cannon(False), None],
        [Pawn(False), None, Pawn(False), None, Pawn(False), None, None, Rook(True), Pawn(False)],
        [None, None, None, None, None, None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [Pawn(True), None, Pawn(True), None, Pawn(True), None, Pawn(True), None, Pawn(True)],
        [None, Cannon(True), None, None, Cannon(True), None, Horse(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [Rook(True), Horse(True), Elephant(True), Advisor(True), King(True), Advisor(True), Elephant(True), None, None],
    ])

def test_move_notation_no_duplicate():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Pawn(True), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Horse(True), None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Cannon(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Rook(True), None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    move = Move(Horse, (5, 0), (3, 1))
    assert move.to_notation(board) == 'H9+8'
    move = Move(Horse, (5, 0), (6, 2))
    assert move.to_notation(board) == 'H9-7'
    move = Move(Cannon, (6, 6), (3, 6))
    assert move.to_notation(board) == 'C3+3'
    move = Move(Rook, (8, 7), (8, 0))
    assert move.to_notation(board) == 'R2.9'
    move = Move(Rook, (8, 7), (9, 7))
    assert move.to_notation(board) == 'R2-1'
    move = Move(Pawn, (2, 2), (2, 1))
    assert move.to_notation(board) == 'P7.8'

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, Cannon(False), None, None, None, None, None, None, None],
        [None, Rook(False), None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Horse(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Pawn(False), None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, Horse(True), None, None, King(True), None, None, None, None],
    ], turn=False)
    move = Move(Cannon, (2, 1), (9, 1))
    assert move.to_notation(board) == 'C2+7'
    move = Move(Cannon, (2, 1), (0, 1))
    assert move.to_notation(board) == 'C2-2'
    move = Move(Rook, (3, 1), (3, 4))
    assert move.to_notation(board) == 'R2.5'
    move = Move(Horse, (4, 6), (5, 4))
    assert move.to_notation(board) == 'H7+5'
    move = Move(Horse, (4, 6), (2, 7))
    assert move.to_notation(board) == 'H7-8'
    move = Move(Pawn, (6, 7), (7, 7))
    assert move.to_notation(board) == 'P8+1'

def test_move_notation_duplicate():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, Horse(True), None, None],
        [None, None, Pawn(True), None, None, None, None, None, None],
        [None, None, None, None, None, None, Horse(True), None, None],
        [None, None, Pawn(True), None, None, None, None, None, None],
        [None, Rook(True), None, None, None, None, Elephant(True), None, None],
        [None, None, Pawn(True), None, None, None, None, None, Cannon(True)],
        [None, Rook(True), None, Advisor(True), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, Cannon(True)],
        [None, None, None, Advisor(True), King(True), None, Elephant(True), None, None],
    ])
    move = Move(Rook, (5, 1), (4, 1))
    assert move.to_notation(board) == '+R+1'
    move = Move(Rook, (7, 1), (7, 2))
    assert move.to_notation(board) == '-R.7'
    move = Move(Pawn, (2, 2), (1, 2))
    assert move.to_notation(board) == '17+1'
    move = Move(Pawn, (4, 2), (4, 3))
    assert move.to_notation(board) == '27.6'
    move = Move(Pawn, (6, 2), (5, 2))
    assert move.to_notation(board) == '37+1'
    move = Move(Advisor, (7, 3), (8, 4))
    assert move.to_notation(board) == '+A-5'
    move = Move(Advisor, (9, 3), (8, 4))
    assert move.to_notation(board) == '-A+5'
    move = Move(Elephant, (5, 6), (7, 4))
    assert move.to_notation(board) == '+E-5'
    move = Move(Elephant, (9, 6), (7, 8))
    assert move.to_notation(board) == '-E+1'
    move = Move(Horse, (1, 6), (0, 8))
    assert move.to_notation(board) == '+H+1'
    move = Move(Horse, (3, 6), (1, 5))
    assert move.to_notation(board) == '-H+4'
    move = Move(Cannon, (8, 8), (9, 8))
    assert move.to_notation(board) == '-C-1'

    board = Xiangqi(board=[
        [None, None, None, King(False), None, Advisor(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, Advisor(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Pawn(False), None],
        [None, None, None, None, None, None, None, Pawn(False), None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ], turn=False)
    move = Move(Advisor, (0, 5), (1, 4))
    assert move.to_notation(board) == '-A+5'
    move = Move(Advisor, (2, 5), (1, 4))
    assert move.to_notation(board) == '+A-5'
    move = Move(Pawn, (6, 7), (6, 6))
    assert move.to_notation(board) == '-P.7'
    move = Move(Pawn, (7, 7), (8, 7))
    assert move.to_notation(board) == '+P+1'

def main():
    test_king_move()
    test_advisor_move()
    test_elephant_move()
    test_horse_move()
    test_rook_move()
    test_cannon_move()
    test_pawn_move()
    test_front_back_move()
    test_pawn_order_move()
    test_board_str()
    test_load_board()
    test_move_notation_no_duplicate()
    test_move_notation_duplicate()

if __name__ == '__main__':
    main()
