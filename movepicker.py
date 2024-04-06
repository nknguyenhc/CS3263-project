from utils.xiangqi import Xiangqi, MoveMode, Move, King, Advisor, Elephant, Horse, Rook, Cannon, Pawn, manhanttan_distance
from typing import List

class Pieces:
    KING = King
    ADVISOR = Advisor
    ELEPHANT = Elephant
    HORSE = Horse
    ROOK = Rook
    CANNON = Cannon
    PAWN = Pawn

class MovePicker:
    def move_gen(self, xiangqi: Xiangqi):
        self.xiangqi = xiangqi
        self.moves = xiangqi.actions()
        return self.moves

    def move_order(self, tt_move: Move | None, counter_move: Move | None,
                   history_heuristic: dict | None, mode: int) -> List[Move]:
        """Returns the sorted list of move dicts in the given board,
        in the order that the main search routine should try.

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
        """
        xiangqi = self.xiangqi
        threats, supports = xiangqi.get_threats_and_supports()
        moves = []
        for move in self.moves:
            move_mode = move.get_mode(xiangqi)
            if not (move_mode & mode):
                continue
            move.value = self.score(move, xiangqi, threats, supports,
                                    tt_move, counter_move, history_heuristic)
            moves.append(move)
        moves.sort(key=lambda move: -move.value)
        return moves

    def score(self, move: Move, xiangqi: Xiangqi,
              threats, supports, tt_move, counter_move, history_heuristic: dict):
        """Returns the score of the given move.
        See explanation for move_order above.

        For captures, if value of attacker <= value of victim,
        or if there is no threat at the target position (threat level = 0), it is a good capture,
        otherwise it is a bad capture. Note that SEE is not yet implemented.

        Good captures have value of at least 2000.
        Quiets have value of at most 2000.
        Bad captures have value at most 0.

        For quiets, we calculate the bonus of escaping from capture, and malus for moving towards a capture.
        Forward moves are given a slightly higher priority, and backward moves are given a slightly lower priority.
        King movement from safety position is heavily penalised.
        """
        if move == tt_move:
            return 100000
        if move.mode & MoveMode.QUIET:
            counter_bonus = 2000 if move == counter_move else 0
            history_bonus = history_heuristic.get((move.from_coords, move.to_coords), 0) if history_heuristic else 0
            check_bonus = 500 if move.mode & MoveMode.CHECK else 0
            escape_bonus = self.get_bonus(move, move.from_coords, threats, supports)
            en_prise_malus = -self.get_bonus(move, move.to_coords, threats, supports)
            king_or_forward_bonus = self.get_king_or_forward_bonus(move, xiangqi)
            return history_bonus + counter_bonus + check_bonus + escape_bonus + en_prise_malus + king_or_forward_bonus
        else:
            piece_from = xiangqi.board[move.from_coords[0]][move.from_coords[1]]
            piece_to = xiangqi.board[move.to_coords[0]][move.to_coords[1]]
            piece_count = xiangqi.get_piece_count()
            difference = abs(piece_to.value(move.from_coords, piece_count)) - abs(piece_from.value(move.to_coords, piece_count))
            is_captured_piece_not_threatened = threats[move.to_coords[0]][move.to_coords[1]] == 0
            return 2000 + max(difference, 0) if difference >= 0 or is_captured_piece_not_threatened else difference

    def get_bonus(self, move, position, threats, supports):
        """Obtains the bonus/malus if a piece moves into/away from the position.
        Returns a positive value.
        """
        threat_value = threats[position[0]][position[1]]
        primary_support_value, secondary_support_value, support_piece_position = supports[position[0]][position[1]]
        support_value = primary_support_value if move.from_coords != support_piece_position else secondary_support_value
        if threat_value == 0:
            return 0

        match move.piecetype:
            case Pieces.ROOK:
                if threat_value > 1:
                    return 1500
                elif support_value > 0:
                    return 200
                else:
                    return 1500
            case Pieces.KING:
                return 0 # Do not add bonus on king movement
            case Pieces.HORSE | Pieces.CANNON:
                if threat_value > 2:
                    return 750
                elif support_value > 0:
                    return 100 if threat_value == 2 else 0
                else:
                    return 750
            case Pieces.ADVISOR | Pieces.ELEPHANT | Pieces.PAWN:
                if threat_value > 3:
                    return 400
                elif support_value > 0:
                    return 50 if threat_value == 3 else 0
                else:
                    return 200

    def get_king_or_forward_bonus(self, move: Move, xiangqi: Xiangqi):
        """Returns the reward for the move dependent on whether the move is a king movement.
        If it is a king movement, give a reward/penalty according to manhattan distance from the safety position.
        Otherwise, reward if it is a forward move, penalise if it is a backward move.
        """
        match move.piecetype:
            case Pieces.KING:
                safety_position = (9, 4) if xiangqi.turn else (0, 4)
                return (manhanttan_distance(move.from_coords, safety_position) - manhanttan_distance(move.to_coords, safety_position)) * 450
            case Pieces.ROOK | Pieces.HORSE | Pieces.CANNON | Pieces.PAWN:
                return move.from_coords[0] - move.to_coords[0] if xiangqi.turn else move.to_coords[0] - move.from_coords[0]
            case Pieces.ADVISOR | Pieces.ELEPHANT:
                return 0
