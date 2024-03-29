from utils.xiangqi import Xiangqi

class Evaluation:
    def evaluate(self, xiangqi: Xiangqi):
        # count the number of pieces, for material value of cannons and horses
        piece_count = xiangqi.get_piece_count()

        # calculate material value and piece activities
        red_value = 0 # will be a positive value
        black_value = 0 # will be a negative value
        for row, arr in enumerate(xiangqi.board):
            for col, piece in enumerate(arr):
                if piece is None:
                    continue
                # print(piece, piece.value((row, col)), piece.activity(xiangqi, (row, col)))
                piece_value = piece.value((row, col), piece_count) * piece.activity(xiangqi, (row, col))
                if piece_value > 0:
                    red_value += piece_value
                else:
                    black_value += piece_value
        
        # calculate bonus for specific piece positions
        values = (red_value, black_value)
        bonus = 0
        for row, arr in enumerate(xiangqi.board):
            for col, piece in enumerate(arr):
                if piece is None:
                    continue
                # print(piece, piece.bonus(xiangqi, (row, col), values))
                bonus += piece.bonus(xiangqi, (row, col), values)
        
        # add value to the side taking the turn
        turn_value = 50 if xiangqi.turn else -50
        return red_value + black_value + bonus + turn_value
