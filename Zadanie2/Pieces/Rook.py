from Pieces.PiecesBlueprint import Figure


class Rook(Figure):
    def simulate_move(self, board):
        return (self.move_right(board) +
                self.move_left(board) +
                self.move_up(board) +
                self.move_down(board)
                )
