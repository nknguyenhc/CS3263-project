from copy import deepcopy

class Xiangqi():
    def __init__(self, board=None, turn=True):
        """Instantiates a new board.
        Board is either not given, which means a default board,
        or an array of 10x9, each element is either None or an instance of Piece class.
        If board is given, assume that it is valid.
        Turn is true if it is red player's turn (first), or False if it is black player's turn (second).
        We do deepcopy here to prevent shared usage elsewhere.
        """
        if board:
            self.board = deepcopy(board)
        else:
            self.board = [
                [Rook(False), Horse(False), Elephant(False), Advisor(False), King(False),
                    Advisor(False), Elephant(False), Horse(False), Rook(False)],
                [None, None, None, None, None, None, None, None, None],
                [None, Cannon(False), None, None, None, None, None, Cannon(False), None],
                [Pawn(False), None, Pawn(False), None, Pawn(False), None, Pawn(False),
                    None, Pawn(False)]
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [Pawn(True), None, Pawn(True), None, Pawn(True), None, Pawn(True),
                    None, Pawn(True)],
                [None, Cannon(True), None, None, None, None, None, Cannon(True), None],
                [None, None, None, None, None, None, None, None, None],
                [Rook(True), Horse(True), Elephant(True), Advisor(True), King(True),
                    Advisor(True), Elephant(True), Horse(True), Rook(True)],
            ]
        self.turn = turn
    
    def actions(self):
        """Returns a list of actions available at this state.
        """
        actions = []
        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                if piece is None:
                    continue
                for action in piece.actions(self, (i, j)):
                    actions.append(action)
        return actions
    
    def can_move_to(self, position):
        """Checks if the position is available that another piece can move to.
        Assuming that the given position is a valid position in the board.
        This means either the slot is empty, or the slot is occupied by a piece of the opposite side.
        """
        piece = self.board[position[0]][position[1]]
        if piece is None:
            return True
        return piece.turn != self.turn
    
    def move(self, action, in_place=False):
        """Returns a new board from application of given action on this board.
        Assuming that the action is a valid action.
        """
        next_state = self if in_place else Xiangqi(board=self.board, turn=not self.turn)
        next_state.board[action.to_coords[0]][action.to_coords[1]] = next_state.board[
            action.from_coords[0]][action.from_coords[1]]
        next_state.board[action.from_coords[0]][action.from_coords[1]] = None
        return next_state


class Move:
    def __init__(self, piecetype, from_coords, to_coords):
        """Instantiates a new move object.
        piecetype is the class associated with the piece.
        from_coords is a tuple of two numbers representing the starting position of the piece (array indices)
        to_coords is a tuple of two numbers representing the ending position of the piece (array indices)
        """
        self.piecetype = piecetype
        self.from_coords = from_coords
        self.to_coords = to_coords
    
    def __hash__(self):
        return hash((self.piecetype, self.from_coords, self.to_coords))
    
    def __eq__(self, other):
        if not isinstance(other, Move):
            return False
        return self.piecetype == other.piecetype and self.from_coords == other.from_coords \
            and self.to_coords == other.to_coords
    
    def __str__(self):
        return f"{self.piecetype.to_string()} {self.from_coords} {self.to_coords}"
    
    def __repr__(self):
        return self.__str__()


class Piece:
    def __init__(self, turn):
        """Instantiates a new piece.
        turn determines whether this piece belongs to red player (first player).
        This is an abstract class.
        """
        self.turn = turn
    
    def actions(self, xiangqi, position):
        """Returns the list of actions possible for this piece,
        given the state and its current position on the board.
        Assuming that the position given is a valid board position of this piece.
        Subclasses should override this method.
        """
        raise NotImplementedError
    
    def to_string():
        """Returns the string representation of the class,
        not associated with any particular instance.
        Subclasses should override this method.
        """
        raise NotImplementedError
    
    def __str__(self):
        return f"{self.__class__.to_string()}{0 if self.turn else 1}"
    
    def __repr__(self):
        return self.__str__()


class King(Piece):
    def __init__(self, turn):
        super().__init__(turn)
    
    def actions(self, xiangqi, position):
        if xiangqi.turn != self.turn:
            return []
        
        actions = []
        if position[0] + 1 <= (9 if self.turn else 2) and xiangqi.can_move_to((position[0] + 1, position[1])):
            actions.append(Move(King, position, (position[0] + 1, position[1])))
        if position[0] - 1 >= (7 if self.turn else 0) and xiangqi.can_move_to((position[0] - 1, position[1])):
            actions.append(Move(King, position, (position[0] - 1, position[1])))
        if position[1] + 1 <= 5 and xiangqi.can_move_to((position[0], position[1] + 1)) \
                and not self.is_move_exposing_kings(position[1] + 1, xiangqi, position[0]):
            actions.append(Move(King, position, (position[0], position[1] + 1)))
        if position[1] - 1 >= 3 and xiangqi.can_move_to((position[0], position[1] - 1)) \
                and not self.is_move_exposing_kings(position[1] - 1, xiangqi, position[0]):
            actions.append(Move(King, position, (position[0], position[1] - 1)))
        return actions
    
    def is_move_exposing_kings(self, col_index, xiangqi, from_row):
        """Checks if the column with given index in the state has any piece blocking in between,
        so that this King piece can move sideway to that column.
        Returns True if the move would expose the two kings.
        """
        for i in (range(from_row - 1, -1, -1) if self.turn else range(from_row + 1, 10)):
            if xiangqi.board[i][col_index] is None:
                continue
            if isinstance(xiangqi.board[i][col_index], King):
                return True
            else:
                return False
        return False
    
    def to_string():
        return 'K'


class Advisor(Piece):
    def __init__(self, turn):
        super().__init__(turn)
    
    def actions(self, xiangqi, position):
        if xiangqi.turn != self.turn:
            return []
        
        if self.turn:
            match position:
                case (9, 3) | (9, 5) | (7, 3) | (7, 5):
                    if xiangqi.can_move_to((8, 4)):
                        return [Move(Advisor, position, (8, 4))]
                    else:
                        return []
                case (8, 4):
                    actions = []
                    for dest in [(9, 3), (9, 5), (7, 3), (7, 5)]:
                        if xiangqi.can_move_to(dest):
                            actions.append(Move(Advisor, position, dest))
                    return actions
        else:
            match position:
                case (0, 3) | (0, 5) | (2, 3) | (2, 5):
                    if xiangqi.can_move_to((1, 4)):
                        return [Move(Advisor, position, (1, 4))]
                    else:
                        return []
                case (1, 4):
                    actions = []
                    for dest in [(0, 3), (0, 5), (2, 3), (2, 5)]:
                        if xiangqi.can_move_to(dest):
                            actions.append(Move(Advisor, position, dest))
                    return actions
    
    def to_string():
        return 'A'


class Elephant(Piece):
    def __init__(self, turn):
        super().__init__(turn)
    
    def actions(self, xiangqi, position):
        if xiangqi.turn != self.turn:
            return []
        
        if self.turn:
            min_row = 5
            max_row = 9
        else:
            min_row = 0
            max_row = 4
        
        actions = []
        if position[0] + 2 <= max_row and position[1] + 2 <= 8 and xiangqi.board[position[0] + 1][position[1] + 1] is None \
                and xiangqi.can_move_to((position[0] + 2, position[1] + 2)):
            actions.append(Move(Elephant, position, (position[0] + 2, position[1] + 2)))
        if position[0] + 2 <= max_row and position[1] - 2 >= 0 and xiangqi.board[position[0] + 1][position[1] - 1] is None \
                and xiangqi.can_move_to((position[0] + 2, position[1] - 2)):
            actions.append(Move(Elephant, position, (position[0] + 2, position[1] - 2)))
        if position[0] - 2 >= min_row and position[1] + 2 <= 8 and xiangqi.board[position[0] - 1][position[1] + 1] is None \
                and xiangqi.can_move_to((position[0] - 2, position[1] + 2)):
            actions.append(Move(Elephant, position, (position[0] - 2, position[1] + 2)))
        if position[0] - 2 >= min_row and position[1] - 2 >= 0 and xiangqi.board[position[0] - 1][position[1] - 1] is None \
                and xiangqi.can_move_to((position[0] - 2, position[1] - 2)):
            actions.append(Move(Elephant, position, (position[0] - 2, position[1] - 2)))
        return actions
    
    def to_string():
        return 'E'


class Horse(Piece):
    def __init__(self, turn):
        super().__init__(turn)
    
    def actions(self, xiangqi, position):
        if xiangqi.turn != self.turn:
            return []
        
        actions = []
        if position[0] + 2 <= 9 and xiangqi.board[position[0] + 1][position[1]] is None:
            if position[1] + 1 <= 8 and xiangqi.can_move_to((position[0] + 2, position[1] + 1)):
                actions.append(Move(Horse, position, (position[0] + 2, position[1] + 1)))
            if position[1] - 1 >= 0 and xiangqi.can_move_to((position[0] + 2, position[1] - 1)):
                actions.append(Move(Horse, position, (position[0] + 2, position[1] - 1)))
        if position[0] - 2 >= 0 and xiangqi.board[position[0] - 1][position[1]] is None:
            if position[1] + 1 <= 8 and xiangqi.can_move_to((position[0] - 2, position[1] + 1)):
                actions.append(Move(Horse, position, (position[0] - 2, position[1] + 1)))
            if position[1] - 1 >= 0 and xiangqi.can_move_to((position[0] - 2, position[1] - 1)):
                actions.append(Move(Horse, position, (position[0] - 2, position[1] - 1)))
        if position[1] + 2 <= 8 and xiangqi.board[position[0]][position[1] + 1] is None:
            if position[0] + 1 <= 9 and xiangqi.can_move_to((position[0] + 1, position[1] + 2)):
                actions.append(Move(Horse, position, (position[0] + 1, position[1] + 2)))
            if position[0] - 1 >= 0 and xiangqi.can_move_to((position[0] - 1, position[1] + 2)):
                actions.append(Move(Horse, position, (position[0] - 1, position[1] + 2)))
        if position[1] - 2 >= 0 and xiangqi.board[position[0]][position[1] - 1] is None:
            if position[0] + 1 <= 9 and xiangqi.can_move_to((position[0] + 1, position[1] - 2)):
                actions.append(Move(Horse, position, (position[0] + 1, position[1] - 2)))
            if position[0] - 1 >= 0 and xiangqi.can_move_to((position[0] - 1, position[1] - 2)):
                actions.append(Move(Horse, position, (position[0] - 1, position[1] - 2)))
        return actions
    
    def to_string():
        return 'H'


class Rook(Piece):
    def __init__(self, turn):
        super().__init__(turn)
    
    def actions(self, xiangqi, position):
        if xiangqi.turn != self.turn:
            return []
        
        actions = []
        for i in range(position[0] + 1, 10):
            if xiangqi.board[i][position[1]] is None:
                actions.append(Move(Rook, position, (i, position[1])))
                continue
            if xiangqi.board[i][position[1]].turn != self.turn:
                actions.append(Move(Rook, position, (i, position[1])))
            break
        for i in range(position[0] - 1, -1, -1):
            if xiangqi.board[i][position[1]] is None:
                actions.append(Move(Rook, position, (i, position[1])))
                continue
            if xiangqi.board[i][position[1]].turn != self.turn:
                actions.append(Move(Rook, position, (i, position[1])))
            break
        for j in range(position[1] + 1, 9):
            if xiangqi.board[position[0]][j] is None:
                actions.append(Move(Rook, position, (position[0], j)))
                continue
            if xiangqi.board[position[0]][j].turn != self.turn:
                actions.append(Move(Rook, position, (position[0], j)))
            break
        for j in range(position[1] - 1, -1, -1):
            if xiangqi.board[position[0]][j] is None:
                actions.append(Move(Rook, position, (position[0], j)))
                continue
            if xiangqi.board[position[0]][j].turn != self.turn:
                actions.append(Move(Rook, position, (position[0], j)))
            break
        return actions
    
    def to_string():
        return 'R'


class Cannon(Piece):
    def __init__(self, turn):
        super().__init__(turn)
    
    def actions(self, xiangqi, position):
        if xiangqi.turn != self.turn:
            return []
        
        actions = []
        for i in range(position[0] + 1, 10):
            if xiangqi.board[i][position[1]] is None:
                actions.append(Move(Cannon, position, (i, position[1])))
                continue
            for ii in range(i + 1, 10):
                if xiangqi.board[ii][position[1]] is not None and xiangqi.board[ii][position[1]].turn != self.turn:
                    actions.append(Move(Cannon, position, (ii, position[1])))
                    break
            break
        for i in range(position[0] - 1, -1, -1):
            if xiangqi.board[i][position[1]] is None:
                actions.append(Move(Cannon, position, (i, position[1])))
                continue
            for ii in range(i - 1, -1, -1):
                if xiangqi.board[ii][position[1]] is not None and xiangqi.board[ii][position[1]].turn != self.turn:
                    actions.append(Move(Cannon, position, (ii, position[1])))
                    break
            break
        for j in range(position[1] + 1, 9):
            if xiangqi.board[position[0]][j] is None:
                actions.append(Move(Cannon, position, (position[0], j)))
                continue
            for jj in range(j + 1, 9):
                if xiangqi.board[position[0]][jj] is not None and xiangqi.board[position[0]][jj].turn != self.turn:
                    actions.append(Move(Cannon, position, (position[0], jj)))
                    break
            break
        for j in range(position[1] - 1, -1, -1):
            if xiangqi.board[position[0]][j] is None:
                actions.append(Move(Cannon, position, (position[0], j)))
                continue
            for jj in range(j - 1, -1, -1):
                if xiangqi.board[position[0]][jj] is not None and xiangqi.board[position[0]][jj].turn != self.turn:
                    actions.append(Move(Cannon, position, (position[0], jj)))
                    break
            break
        return actions
    
    def to_string():
        return 'C'


class Pawn(Piece):
    def __init__(self, turn):
        super().__init__(turn)
    
    def actions(self, xiangqi, position):
        if xiangqi.turn != self.turn:
            return []
        
        actions = []
        if self.turn:
            if position[0] > 0 and xiangqi.can_move_to((position[0] - 1, position[1])):
                actions.append(Move(Pawn, position, (position[0] - 1, position[1])))
            if position[0] <= 4:
                if position[1] > 0 and xiangqi.can_move_to((position[0], position[1] - 1)):
                    actions.append(Move(Pawn, position, (position[0], position[1] - 1)))
                if position[1] < 8 and xiangqi.can_move_to((position[0], position[1] + 1)):
                    actions.append(Move(Pawn, position, (position[0], position[1] + 1)))
        else:
            if position[0] < 9 and xiangqi.can_move_to((position[0] + 1, position[1])):
                actions.append(Move(Pawn, position, (position[0] + 1, position[1])))
            if position[0] >= 5:
                if position[1] > 0 and xiangqi.can_move_to((position[0], position[1] - 1)):
                    actions.append(Move(Pawn, position, (position[0], position[1] - 1)))
                if position[1] < 8 and xiangqi.can_move_to((position[0], position[1] + 1)):
                    actions.append(Move(Pawn, position, (position[0], position[1] + 1)))
        return actions
    
    def to_string():
        return 'P'
