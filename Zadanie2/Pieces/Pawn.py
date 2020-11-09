from Pieces.PiecesBlueprint import Figure


class Pawn(Figure):
    def simulate_move(self, board):
        if self.color == "w":
            moves = (self.move_up_by_one(board) +
                     self.move_up_left_by_one(board) +
                     self.move_up_right_by_one(board)
                     )
            if self.get_y() == 6:
                moves = moves + self.move_up_by_two(board)
        else:
            moves = (self.move_down_by_one(board) +
                     self.move_down_left_by_one(board) +
                     self.move_down_right_by_one(board)
                     )
            if self.get_y() == 1:
                moves = moves + self.move_down_by_two(board)
        return moves

    def simulate_attack(self, board):
        if self.color == "w":
            moves = (self.move_up_left_by_one(board) +
                     self.move_up_right_by_one(board)
                     )
        else:
            moves = (self.move_down_left_by_one(board) +
                     self.move_down_right_by_one(board)
                     )
        return moves
