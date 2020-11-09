from Pieces.PiecesBlueprint import Figure


class Knight(Figure):
    def simulate_move(self, board):
        return self.move_like_knight(board)
