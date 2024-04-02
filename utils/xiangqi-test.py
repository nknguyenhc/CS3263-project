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
    assert set(King(True).get_reachable_cells(board, (8, 4))) == {
        (9, 4), (7, 4), (8, 5),
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
    assert set(King(False).get_reachable_cells(board, (0, 3))) == {(1, 3)}

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
    assert set(King(True).get_reachable_cells(board, (8, 5))) == {
        (9, 5), (7, 5), (8, 4),
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
    assert set(King(False).get_reachable_cells(board, (0, 3))) == {
        (1, 3), (0, 4),
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
    assert set(King(True).get_reachable_cells(board, (8, 3))) == {
        (9, 3), (7, 3), (8, 4),
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
    assert set(King(False).get_reachable_cells(board, (1, 3))) == {
        (0, 3), (2, 3), (1, 4),
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
    assert set(Advisor(True).get_reachable_cells(board, (9, 5))) == {(8, 4)}
    assert set(Advisor(True).get_reachable_cells(board, (9, 3))) == {(8, 4)}
    assert set(King(True).get_reachable_cells(board, (9, 4))) == {
        (8, 4), (9, 5),
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
    assert set(Advisor(True).get_reachable_cells(board, (8, 4))) == {
        (7, 3), (7, 5), (9, 3), (9, 5),
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
    assert set(Elephant(True).get_reachable_cells(board, (9, 6))) == {
        (7, 8), (7, 4),
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
    assert set(Elephant(True).get_reachable_cells(board, (9, 6))) == {(7, 8)}

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
    assert set(Elephant(True).get_reachable_cells(board, (7, 8))) == {
        (9, 6), (5, 6),
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
    assert set(Elephant(True).get_reachable_cells(board, (7, 4))) == {
        (9, 2), (5, 2), (5, 6),
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
    assert set(Elephant(False).get_reachable_cells(board, (2, 4))) == {
        (0, 6), (4, 2), (4, 6),
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
    assert set(Horse(True).get_reachable_cells(board, (5, 3))) == {
        (7, 4), (6, 5), (4, 5), (3, 4), (3, 2), (4, 1), (6, 1), (7, 2),
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
    assert set(Horse(True).get_reachable_cells(board, (5, 3))) == {
        (7, 4), (6, 5), (4, 5), (3, 4), (3, 2), (7, 2),
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
    assert set(Horse(True).get_reachable_cells(board, (9, 6))) == {
        (7, 5), (7, 7), (8, 8),
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
    assert set(Horse(True).get_reachable_cells(board, (8, 6))) == {
        (9, 4), (7, 4), (6, 5), (6, 7), (7, 8), (9, 8),
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
    assert set(Rook(True).get_reachable_cells(board, (7, 6))) == {
        (8, 6), (9, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6), (0, 6),
        (7, 7), (7, 8), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0),
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
    assert set(Rook(True).get_reachable_cells(board, (7, 6))) == {
        (8, 6), (9, 6), (6, 6), (5, 6), (4, 6), (3, 6),
        (7, 7), (7, 8), (7, 5), (7, 4), (7, 3),
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
    assert set(Cannon(True).get_reachable_cells(board, (7, 6))) == set()

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
    assert set(Cannon(True).get_reachable_cells(board, (7, 6))) == {
        (0, 6), (1, 6), (2, 6),
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
    assert set(Cannon(True).get_reachable_cells(board, (7, 6))) == {
        (1, 6), (2, 6), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, Elephant(False), None, None],
        [None, None, None, None, None, None, Pawn(True), None, None],
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
        Move(Cannon, (7, 6), (7, 7)),
        Move(Cannon, (7, 6), (7, 8)),
        Move(Cannon, (7, 6), (7, 0)),
        Move(Pawn, (1, 6), (1, 5)),
        Move(Pawn, (1, 6), (1, 7)),
        Move(Pawn, (1, 6), (0, 6)),
    }
    assert set(Cannon(True).get_reachable_cells(board, (7, 6))) == {
        (1, 6), (2, 6), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0),
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
    assert set(Pawn(True).get_reachable_cells(board, (3, 6))) == {
        (3, 7), (3, 5), (2, 6),
    }
    assert set(Pawn(True).get_reachable_cells(board, (6, 0))) == {(5, 0)}

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
    assert set(Pawn(False).get_reachable_cells(board, (3, 6))) == {(4, 6)}
    assert set(Pawn(False).get_reachable_cells(board, (6, 0))) == {
        (6, 1), (7, 0),
    }

def test_rook_discover_check_constraint():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 5)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 5)),
        Move(King, (9, 4), (8, 4)),
        Move(Cannon, (7, 4), (8, 4)),
        Move(Cannon, (7, 4), (6, 4)),
        Move(Cannon, (7, 4), (5, 4)),
        Move(Cannon, (7, 4), (4, 4)),
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
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, Rook(True), Rook(False), None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (8, 4)),
        Move(King, (9, 4), (9, 5)),
        Move(Rook, (9, 6), (9, 5)),
        Move(Rook, (9, 6), (9, 7)),
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
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), Horse(False), None, Rook(False), None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (8, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 5)),
        Move(Advisor, (8, 4), (9, 3)),
        Move(Advisor, (8, 4), (9, 5)),
        Move(Advisor, (8, 4), (7, 3)),
        Move(Advisor, (8, 4), (7, 5)),
        Move(Elephant, (7, 4), (5, 2)),
        Move(Elephant, (7, 4), (5, 6)),
        Move(Elephant, (7, 4), (9, 2)),
        Move(Elephant, (7, 4), (9, 6)),
    }

def test_cannon_discover_two_pieces_check_constraint():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 5)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, Horse(True), King(True), Advisor(True), Elephant(True), Cannon(False), None],
    ])
    assert set(board.actions()) == {
        Move(Horse, (9, 3), (7, 2)),
        Move(Horse, (9, 3), (8, 1)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, None, King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Rook, (6, 4), (7, 4)),
        Move(Rook, (6, 4), (5, 4)),
        Move(Rook, (6, 4), (4, 4)),
    }
    
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, Rook(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 5)),
        Move(King, (9, 4), (8, 4)),
        Move(Rook, (7, 4), (8, 4)),
        Move(Rook, (7, 4), (6, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, Horse(False), None, None, None, None],
        [None, None, None, None, King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Advisor, (9, 5), (8, 4))
    }

def test_cannon_discover_no_piece_check_constraint():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Pawn(True), None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Elephant(True), Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (8, 4)),
        Move(Pawn, (3, 3), (3, 2)),
        Move(Pawn, (3, 3), (3, 4)),
        Move(Pawn, (3, 3), (2, 3)),
        Move(Elephant, (9, 2), (7, 0)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, Rook(True), None, None, Elephant(True)],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, Advisor(True), King(True), None, Cannon(False), None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 5)),
        Move(Advisor, (8, 4), (7, 3)),
        Move(Rook, (7, 5), (8, 5)),
        Move(Rook, (7, 5), (6, 5)),
        Move(Rook, (7, 5), (5, 5)),
        Move(Rook, (7, 5), (4, 5)),
        Move(Rook, (7, 5), (3, 5)),
        Move(Rook, (7, 5), (2, 5)),
        Move(Rook, (7, 5), (1, 5)),
        Move(Rook, (7, 5), (0, 5)),
        Move(Rook, (7, 5), (7, 4)),
        Move(Rook, (7, 5), (7, 3)),
        Move(Rook, (7, 5), (7, 2)),
        Move(Rook, (7, 5), (7, 1)),
        Move(Rook, (7, 5), (7, 0)),
        Move(Rook, (7, 5), (7, 6)),
        Move(Rook, (7, 5), (7, 7)),
        Move(Elephant, (7, 8), (5, 6)),
        Move(Elephant, (7, 8), (9, 6)),
    }

def test_horse_discover_check_constraint():
    board = Xiangqi([
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Horse(False), None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, King(True), None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 3), (8, 3)),
        Move(King, (9, 3), (9, 4)),
    }

    board = Xiangqi([
        [None, None, None, None, None, King(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Horse(False), Rook(True), None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Rook, (8, 3), (8, 2)),
        Move(King, (9, 4), (8, 4)),
        Move(Advisor, (9, 3), (8, 4)),
    }

def test_pawn_discover_check_constraint():
    board = Xiangqi([
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
        [None, None, None, None, None, Pawn(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (7, 4), (7, 5)),
    }

    board = Xiangqi([
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Pawn(False), None, None],
        [None, None, None, None, None, King(True), None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 5), (8, 4)),
        Move(King, (8, 5), (9, 5)),
    }

    board = Xiangqi([
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, Pawn(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ], turn=False)
    assert set(board.actions()) == set()

    board = Xiangqi([
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Pawn(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 4), (9, 4)),
    }

def test_king_discover_check_constraint():
    board = Xiangqi([
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Horse(True), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 3)),
        Move(King, (9, 4), (9, 5)),
    }

    board = Xiangqi([
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Horse(False), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 3)),
        Move(King, (9, 4), (9, 5)),
    }

    board = Xiangqi([
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(True), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 3)),
        Move(King, (9, 4), (9, 5)),
        Move(Cannon, (8, 4), (7, 4)),
        Move(Cannon, (8, 4), (6, 4)),
        Move(Cannon, (8, 4), (5, 4)),
        Move(Cannon, (8, 4), (4, 4)),
        Move(Cannon, (8, 4), (3, 4)),
        Move(Cannon, (8, 4), (2, 4)),
        Move(Cannon, (8, 4), (1, 4)),
    }

    board = Xiangqi([
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 3)),
        Move(King, (9, 4), (9, 5)),
        Move(Advisor, (8, 4), (9, 3)),
        Move(Advisor, (8, 4), (9, 5)),
        Move(Advisor, (8, 4), (7, 3)),
        Move(Advisor, (8, 4), (7, 5)),
        Move(Elephant, (7, 4), (9, 2)),
        Move(Elephant, (7, 4), (9, 6)),
        Move(Elephant, (7, 4), (5, 2)),
        Move(Elephant, (7, 4), (5, 6)),
    }

def test_rook_check_constraint():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, Rook(True), None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Advisor, (9, 3), (8, 4)),
        Move(Advisor, (9, 5), (8, 4)),
        Move(Rook, (6, 1), (6, 4)),
    }
    
    board = Xiangqi(board=[
        [Rook(True), None, None, None, King(False), None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Rook(False), None, None, Cannon(False), None, King(True), None, None, None],
    ], turn=False)
    assert set(board.actions()) == {
        Move(Cannon, (9, 3), (0, 3)),
        Move(Rook, (9, 0), (0, 0)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, None, King(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, Rook(False), None, King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == set()

    board = Xiangqi(board=[
        [None, None, None, None, None, King(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, Rook(False), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 3)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, Rook(False), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == set()

def test_cannon_check_constraint():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, Rook(True), None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 5)),
        Move(Advisor, (9, 3), (8, 4)),
        Move(Elephant, (7, 4), (9, 2)),
        Move(Elephant, (7, 4), (9, 6)),
        Move(Elephant, (7, 4), (5, 2)),
        Move(Elephant, (7, 4), (5, 6)),
        Move(Rook, (6, 1), (6, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, Rook(True), None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, Rook(True), None, None, Horse(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Rook, (4, 1), (4, 4)),
        Move(Advisor, (9, 3), (8, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Rook(True), None, Cannon(False), None, None, None, None],
        [None, None, Rook(True), None, Rook(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Advisor, (9, 3), (8, 4)),
        Move(Advisor, (9, 5), (8, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == set()

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Pawn(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, Rook(True), Cannon(True), Rook(True), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Advisor, (9, 5), (8, 4)),
        Move(Advisor, (9, 3), (8, 4)),
        Move(Cannon, (7, 4), (3, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(False), None, None, None, None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (8, 4))
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(False), None, None, Rook(False), None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == set()

def test_horse_check_constraint():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Elephant(True), Horse(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (8, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, Horse(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Horse(False), None, None, None, None, None, None],
        [None, None, None, Advisor(True), King(True), Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(Horse, (6, 4), (8, 3)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, Cannon(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, Horse(True), None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, None, None, King(True), None, Horse(False), Cannon(False)],
    ])
    assert set(board.actions()) == {
        Move(Horse, (7, 5), (9, 6)),
    }

def test_pawn_check_constraint():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Rook(True), None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Pawn(False), None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 4), (9, 5)),
        Move(King, (9, 4), (8, 4)),
    }

    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Rook(True), None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Pawn(False), Pawn(False), None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    assert set(board.actions()) == set()

def test_rook_constraining_king():
    board = Xiangqi(board=[
        [None, None, None, King(False), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Rook(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, King(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 5), (8, 5)),
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
        [None, None, None, Advisor(True), None, Advisor(True), Rook(False), None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 4), (9, 4)),
        Move(King, (8, 4), (7, 4)),
        Move(King, (8, 4), (8, 5)),
    }

def test_cannon_constrain_king():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, King(True), None, Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 3), (8, 3)),
        Move(Advisor, (8, 4), (7, 3)),
        Move(Advisor, (8, 4), (7, 5)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(False), None, None, None, None],
        [None, None, None, None, Pawn(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Advisor(True), None, None, None, None],
        [None, None, None, King(True), None, Advisor(True), None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (9, 3), (9, 4)),
        Move(King, (9, 3), (8, 3)),
        Move(Advisor, (8, 4), (7, 3)),
        Move(Advisor, (8, 4), (7, 5)),
    }

def test_horse_constrain_king():
    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Horse(False), None, None, None, None],
        [None, None, None, None, Elephant(True), Horse(False), None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == {
        Move(King, (8, 4), (8, 5)),
        Move(King, (8, 4), (8, 3)),
    }

    board = Xiangqi(board=[
        [None, None, None, None, King(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Horse(False), None, None, None, None, None, None],
        [None, None, None, King(True), None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    assert set(board.actions()) == set()

def test_comparison():
    board1 = Xiangqi()
    board2 = Xiangqi()
    assert board1 == board2
    assert hash(board1) == hash(board2)

def test_rook_row_reachable_move_count():
    board = Xiangqi(board=[
        [None, Cannon(True), None, None, King(False), None, None, None, None],
        [None, None, None, None, Advisor(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, Rook(True), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    piece = board.board[3][2]
    assert piece.row_reachable_move_count(board, (3, 2), 0, 1, 4) == 1

    board = Xiangqi(board=[
        [None, Cannon(True), None, None, King(False), None, None, None, None],
        [None, None, None, None, Advisor(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Rook(True), None, Pawn(False), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    piece = board.board[3][0]
    assert piece.row_reachable_move_count(board, (3, 0), 0, 1, 4) == 2

    board = Xiangqi(board=[
        [None, None, Cannon(True), None, King(False), None, None, None, None],
        [None, None, None, None, Advisor(False), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [Rook(True), None, Pawn(False), None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ])
    piece = board.board[3][0]
    assert piece.row_reachable_move_count(board, (3, 0), 0, 2, 4) == 0

def test_rook_col_reachable_move_count():
    board = Xiangqi(board=[
        [None, None, None, Advisor(False), King(False), Advisor(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Rook(True), None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    piece = board.board[7][7]
    assert piece.col_reachable_move_count(board, (6, 7), 4, 0, 5) == 2

    board = Xiangqi(board=[
        [None, None, None, Advisor(False), King(False), Advisor(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, Rook(True), None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(True), None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    piece = board.board[3][7]
    assert piece.col_reachable_move_count(board, (3, 7), 4, 0, 5) == 1

    board = Xiangqi(board=[
        [None, None, None, Advisor(False), King(False), Advisor(False), None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Cannon(True), None, Pawn(False), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, Rook(True), None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, King(True), None, None, None, None],
    ])
    piece = board.board[7][6]
    assert piece.col_reachable_move_count(board, (6, 6), 4, 0, 5) == 0

def main():
    test_king_move()
    test_advisor_move()
    test_elephant_move()
    test_horse_move()
    test_rook_move()
    test_cannon_move()
    test_pawn_move()

    test_rook_discover_check_constraint()
    test_cannon_discover_two_pieces_check_constraint()
    test_cannon_discover_no_piece_check_constraint()
    test_horse_discover_check_constraint()
    test_pawn_discover_check_constraint()
    test_king_discover_check_constraint()
    test_rook_check_constraint()
    test_cannon_check_constraint()
    test_horse_check_constraint()
    test_pawn_check_constraint()

    test_comparison()

    test_rook_row_reachable_move_count()
    test_rook_col_reachable_move_count()

if __name__ == '__main__':
    main()
