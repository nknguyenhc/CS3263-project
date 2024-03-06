from xiangqi import Xiangqi, Rook, Horse, Elephant, Advisor, King, Cannon, Pawn, Move

def test_king_move():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Pawn(False), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 4), (9, 4)),
        Move(King, (8, 4), (7, 4)),
        Move(King, (8, 4), (8, 5)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ], turn=False)
    assert set(board.actions()) == {
        Move(King, (0, 3), (1, 3)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 5), (9, 5)),
        Move(King, (8, 5), (7, 5)),
        Move(King, (8, 5), (8, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ], turn=False)
    assert set(board.actions()) == {
        Move(King, (0, 3), (1, 3)),
        Move(King, (0, 3), (0, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Pawn(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, King(True), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 3), (9, 3)),
        Move(King, (8, 3), (7, 3)),
        Move(King, (8, 3), (8, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Pawn(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ], turn=False)
    assert set(board.actions()) == {
        Move(King, (1, 3), (0, 3)),
        Move(King, (1, 3), (2, 3)),
        Move(King, (1, 3), (1, 4)),
    }

def test_advisor_move():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Advisor, (9, 5), (8, 4)),
        Move(Advisor, (9, 3), (8, 4)),
        Move(King, (9, 4), (8, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, None, King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Advisor, (8, 4), (7, 3)),
        Move(Advisor, (8, 4), (7, 5)),
        Move(Advisor, (8, 4), (9, 3)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, Advisor(False), None, None, None, None],
        [None, None, None, None, None, Pawn(True), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ], turn=False)
    assert set(board.actions()) == {
        Move(Advisor, (1, 4), (2, 3)),
        Move(Advisor, (1, 4), (2, 5)),
        Move(Advisor, (1, 4), (0, 5)),
        Move(King, (0, 3), (0, 4)),
        Move(King, (0, 3), (1, 3)),
    }

def test_elephant_move():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), Elephant(True), None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Elephant, (9, 6), (7, 8)),
        Move(Elephant, (9, 6), (7, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
        [None, None, None, None, None, None, Elephant(True), None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 5), (9, 5)),
        Move(King, (8, 5), (7, 5)),
        Move(Elephant, (9, 6), (7, 8)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, Elephant(True)],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Elephant, (7, 8), (9, 6)),
        Move(Elephant, (7, 8), (5, 6)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 5), (7, 5)),
        Move(King, (8, 5), (9, 5)),
        Move(King, (8, 5), (8, 4)),
        Move(Elephant, (7, 4), (9, 2)),
        Move(Elephant, (7, 4), (5, 2)),
        Move(Elephant, (7, 4), (5, 6)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, Elephant(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ], turn=False)
    assert set(board.actions()) == {
        Move(King, (1, 3), (2, 3)),
        Move(King, (1, 3), (0, 3)),
        Move(King, (1, 3), (1, 4)),
        Move(Elephant, (2, 4), (0, 6)),
        Move(Elephant, (2, 4), (4, 2)),
        Move(Elephant, (2, 4), (4, 6)),
    }

def test_horse_move():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Horse(True), None, None, None, None, None],
        [None, Pawn(False), None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Horse, (5, 3), (7, 4)),
        Move(Horse, (5, 3), (6, 5)),
        Move(Horse, (5, 3), (4, 5)),
        Move(Horse, (5, 3), (3, 4)),
        Move(Horse, (5, 3), (3, 2)),
        Move(Horse, (5, 3), (4, 1)),
        Move(Horse, (5, 3), (6, 1)),
        Move(Horse, (5, 3), (7, 2)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Pawn(False), Horse(True), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Horse, (5, 3), (7, 4)),
        Move(Horse, (5, 3), (6, 5)),
        Move(Horse, (5, 3), (4, 5)),
        Move(Horse, (5, 3), (3, 4)),
        Move(Horse, (5, 3), (3, 2)),
        Move(Horse, (5, 3), (7, 2)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), Horse(True), None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Horse, (9, 6), (7, 5)),
        Move(Horse, (9, 6), (7, 7)),
        Move(Horse, (9, 6), (8, 8)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Horse(True), None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Horse, (8, 6), (9, 4)),
        Move(Horse, (8, 6), (7, 4)),
        Move(Horse, (8, 6), (6, 5)),
        Move(Horse, (8, 6), (6, 7)),
        Move(Horse, (8, 6), (7, 8)),
        Move(Horse, (8, 6), (9, 8)),
    }

def test_rook_move():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Rook(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Rook, (7, 6), (8, 6)),
        Move(Rook, (7, 6), (9, 6)),
        Move(Rook, (7, 6), (6, 6)),
        Move(Rook, (7, 6), (5, 6)),
        Move(Rook, (7, 6), (4, 6)),
        Move(Rook, (7, 6), (3, 6)),
        Move(Rook, (7, 6), (2, 6)),
        Move(Rook, (7, 6), (1, 6)),
        Move(Rook, (7, 6), (0, 6)),
        Move(Rook, (7, 6), (7, 7)),
        Move(Rook, (7, 6), (7, 8)),
        Move(Rook, (7, 6), (7, 5)),
        Move(Rook, (7, 6), (7, 4)),
        Move(Rook, (7, 6), (7, 3)),
        Move(Rook, (7, 6), (7, 2)),
        Move(Rook, (7, 6), (7, 1)),
        Move(Rook, (7, 6), (7, 0)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, King(True), None, None, Rook(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (7, 3), (8, 3)),
        Move(Rook, (7, 6), (8, 6)),
        Move(Rook, (7, 6), (9, 6)),
        Move(Rook, (7, 6), (6, 6)),
        Move(Rook, (7, 6), (5, 6)),
        Move(Rook, (7, 6), (4, 6)),
        Move(Rook, (7, 6), (3, 6)),
        Move(Rook, (7, 6), (7, 7)),
        Move(Rook, (7, 6), (7, 8)),
        Move(Rook, (7, 6), (7, 5)),
        Move(Rook, (7, 6), (7, 4)),
    }

def test_cannon_move():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Cannon(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Cannon, (7, 6), (8, 6)),
        Move(Cannon, (7, 6), (9, 6)),
        Move(Cannon, (7, 6), (6, 6)),
        Move(Cannon, (7, 6), (5, 6)),
        Move(Cannon, (7, 6), (4, 6)),
        Move(Cannon, (7, 6), (3, 6)),
        Move(Cannon, (7, 6), (2, 6)),
        Move(Cannon, (7, 6), (1, 6)),
        Move(Cannon, (7, 6), (0, 6)),
        Move(Cannon, (7, 6), (7, 7)),
        Move(Cannon, (7, 6), (7, 8)),
        Move(Cannon, (7, 6), (7, 5)),
        Move(Cannon, (7, 6), (7, 4)),
        Move(Cannon, (7, 6), (7, 3)),
        Move(Cannon, (7, 6), (7, 2)),
        Move(Cannon, (7, 6), (7, 1)),
        Move(Cannon, (7, 6), (7, 0)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Pawn(False), None, None, None, None, None, Cannon(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Cannon, (7, 6), (8, 6)),
        Move(Cannon, (7, 6), (9, 6)),
        Move(Cannon, (7, 6), (6, 6)),
        Move(Cannon, (7, 6), (5, 6)),
        Move(Cannon, (7, 6), (4, 6)),
        Move(Cannon, (7, 6), (7, 7)),
        Move(Cannon, (7, 6), (7, 8)),
        Move(Cannon, (7, 6), (7, 5)),
        Move(Cannon, (7, 6), (7, 4)),
        Move(Cannon, (7, 6), (7, 3)),
        Move(Cannon, (7, 6), (7, 2)),
        Move(Cannon, (7, 6), (7, 1)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, Elephant(False), None, None],
        [None, None, None, None, None, None, Cannon(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Pawn(False), None, None, None, None, King(True), Cannon(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (7, 5), (8, 5)),
        Move(Cannon, (7, 6), (8, 6)),
        Move(Cannon, (7, 6), (9, 6)),
        Move(Cannon, (7, 6), (6, 6)),
        Move(Cannon, (7, 6), (5, 6)),
        Move(Cannon, (7, 6), (4, 6)),
        Move(Cannon, (7, 6), (1, 6)),
        Move(Cannon, (7, 6), (7, 7)),
        Move(Cannon, (7, 6), (7, 8)),
        Move(Cannon, (7, 6), (7, 0)),
    }

def test_pawn_move():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Pawn(True), None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
        Move(Pawn, (3, 6), (3, 7)),
        Move(Pawn, (3, 6), (3, 5)),
        Move(Pawn, (3, 6), (2, 6)),
        Move(Pawn, (6, 0), (5, 0)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Pawn(False), None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ], turn=False)
    assert set(board.actions()) == {
        Move(King, (0, 3), (1, 3)),
        Move(Pawn, (3, 6), (4, 6)),
        Move(Pawn, (6, 0), (6, 1)),
        Move(Pawn, (6, 0), (7, 0)),
    }

def test_moves_being_checked():
    """Tests that when the player is being checked, the only available moves are those that respond to the check.
    """
    pass

def test_moves_discover_check():
    """Tests that the moves available do not discover a check from the opponent.
    """
    pass

def main():
    test_king_move()
    test_advisor_move()
    test_elephant_move()
    test_horse_move()
    test_rook_move()
    test_cannon_move()
    test_pawn_move()
    test_moves_being_checked()
    test_moves_discover_check()

if __name__ == '__main__':
    main()
