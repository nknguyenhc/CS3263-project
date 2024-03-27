from utils.xiangqi import Xiangqi, King, Advisor, Elephant, Horse, Rook, Cannon, Pawn

class Pieces:
    KING = King
    ADVISOR = Advisor
    ELEPHANT = Elephant
    HORSE = Horse
    ROOK = Rook
    CANNON = Cannon
    PAWN = Pawn

class MovePicker:
    piece_to_threat = {
        King: 1,
        Rook: 1,
        Horse: 2,
        Cannon: 2,
        Advisor: 3,
        Elephant: 3,
        Pawn: 4,
    }

    def __init__(self, xiangqi):
        """Instantiates a new move picker for the given board position.
        Each move picker corresponds to a board.
        The method next_move of each move picker can be called multiple times
        to get the next moves, in each iteration of a search routine.
        """
        self.xiangqi = xiangqi
        self.moves = self.move_order()
        self.pointer = 0
    
    def move_order(self):
        """Returns the sorted list of move dicts in the given board,
        in the order that the main search routine should try.
        Only to be used in constructor.
        Each move dict contains 3 keys:
        - move: the move itself
        - priority: the priority that this move should be tried (used as sorting key)
        - is_quiet: whether the move is quiet

        Moves are ordered in the following:
        * good captures
        * good quiets
          * bonus for generating checks
          * bonus for escaping captures
          * malus for putting piece en prise (in threat of capture)
        * bad captures
        * bad quiets

        The goodness of a capture move is evaluated using MVV/LVA.
        In future, SEE can also be incorporated.
        MVV/LVA can potentially be improved by incorporating activity of a piece.

        Good quiets do not make use of the search history.
        In future, transposition table can be used to score moves more accurately.

        To obtain the bonus for escaping captures and malus for putting piece en prise,
        we need to get the available actions from the opponent in the current board.
        Bonus for escaping capture only counts when value of attacker < value of victim.
        """
        threats = self.get_threats()
        moves = [
            {
                "move": move,
                "priority": self.score(move, threats),
                "is_quiet": self.is_quiet(move),
            } for move in self.xiangqi.actions()
        ]
        moves.sort(key=lambda x: -x["priority"])
        return moves
    
    def get_threats(self):
        """Get the threats that the enemy poses on each position.
        The returned value is a 2D array, each element corresponds to the position in the board.
        The lower the value of the attacker, the higher the threat.
        Each element has either one of the following value:
        0: no threat
        1: threat by rook/king
        2: threat by cannon/horse
        3: threat by advisor/elephant
        4: threat by pawn
        """
        reverse_board = Xiangqi(
            board=self.xiangqi.board,
            turn=not self.xiangqi.turn,
            king_positions=self.xiangqi.king_positions,
            copy=False)
        threats = [[0 for i in range(9)] for j in range(10)]
        for i, row in enumerate(reverse_board.board):
            for j, piece in enumerate(row):
                if piece is None:
                    continue
                for threatened_cell in piece.get_reachable_cells(reverse_board, (i, j)):
                    ii, jj = threatened_cell
                    threats[ii][jj] = max(threats[ii][jj], MovePicker.piece_to_threat[piece.__class__])
        return threats
    
    def score(self, move, threats):
        """Returns the score of the given move.
        See explanation for move_order above.

        For captures, if value of attacker <= value of victim,
        or if there is no threat at the target position (threat level = 0), it is a good capture,
        otherwise it is a bad capture. Note that SEE is not yet implemented.

        Good captures have value of at least 2000.
        Quiets have value of at most 2000.
        Bad captures have value at most 0.
        """
        if self.is_quiet(move):
            check_bonus = 500 if self.is_check(move) else 0
            escape_bonus = self.get_bonus(move.piecetype, move.from_coords, threats)
            en_prise_malus = -self.get_bonus(move.piecetype, move.to_coords, threats)
            return check_bonus + escape_bonus + en_prise_malus
        else:
            piece_from = self.xiangqi.board[move.from_coords[0]][move.from_coords[1]]
            piece_to = self.xiangqi.board[move.to_coords[0]][move.to_coords[1]]
            difference = abs(piece_to.value(move.from_coords)) - abs(piece_from.value(move.to_coords))
            is_captured_piece_not_threatened = threats[move.to_coords[0]][move.to_coords[1]] == 0
            return 2000 + max(difference, 0) if difference >= 0 or is_captured_piece_not_threatened else difference
        
    def get_bonus(self, piecetype, position, threats):
        """Obtains the bonus/malus if a piece moves into/away from the position.
        Returns a positive value.
        """
        threat_value = threats[position[0]][position[1]]
        match piecetype:
            case Pieces.ROOK:
                return 1500 if threat_value >= 2 else 0
            case Pieces.KING:
                return 0 # Do not add bonus on king movement
            case Pieces.HORSE | Pieces.CANNON:
                return 750 if threat_value >= 3 else 0
            case Pieces.ADVISOR | Pieces.ELEPHANT | Pieces.PAWN:
                return 400 if threat_value >= 4 else 0
    
    def is_check(self, move):
        """Determines if the given move results in a check.
        """
        next_board = self.xiangqi.move(move)
        constraints = next_board.get_constraints()
        return any([constraint.is_check() for constraint in constraints])
    
    def is_quiet(self, move):
        """Determines if the given move is a quiet move, i.e. is not a capture.
        """
        row, col = move.to_coords
        return self.xiangqi.board[row][col] is None
    
    def next_move(self, skip_quiet=False):
        """Returns the next possible move.
        Returns None if there is no possible move.
        skip_quiet indicates whether to not return a quiet move.
        """
        if self.pointer == len(self.moves):
            return None
        
        if not skip_quiet:
            return self.moves[self.pointer]["move"]
        
        while self.pointer < len(self.moves):
            if not self.moves[self.pointer]["is_quiet"]:
                return self.moves[self.pointer]["move"]
            self.pointer += 1
        
        return None
