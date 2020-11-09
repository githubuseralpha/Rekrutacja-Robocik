from Pieces.PiecesBlueprint import Figure


class Bishop(Figure):
    def simulate_move(self, board):
        return (self.move_down_left(board) +
                self.move_down_right(board) +
                self.move_up_left(board) +
                self.move_up_right(board)
                )
