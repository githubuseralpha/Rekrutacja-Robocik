from Pieces.PiecesBlueprint import Figure


class King(Figure):
    def simulate_move(self, board):
        return self.move_by_one(board)
