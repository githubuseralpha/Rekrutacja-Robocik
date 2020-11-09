from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.King import King
from board_functions import *


class Scenario:
    def __init__(self, board, figures, move, index):
        self.board = copy_board(board)
        self.danger_board = copy_board(board)
        self.figures = figures
        self.move = move
        self.index = index

    def add_figure(self, figure):
        self.figures.append(figure)

    def update_figures(self, board):
        for i in range(8):
            for j in range(8):
                type_of_piece = board[i][j][1]
                color = board[i][j][0]
                if type_of_piece == "q":
                    self.add_figure(Queen(j, i, color, type_of_piece))
                if type_of_piece == "r":
                    self.add_figure(Rook(j, i, color, type_of_piece))
                if type_of_piece == "b":
                    self.add_figure(Bishop(j, i, color, type_of_piece))
                if type_of_piece == "k":
                    self.add_figure(Knight(j, i, color, type_of_piece))
                if type_of_piece == "p":
                    self.add_figure(Pawn(j, i, color, type_of_piece))
                if type_of_piece == "W":
                    self.add_figure(King(j, i, color, type_of_piece))

    def get_board(self):
        return self.board

    def get_figures(self):
        return self.figures

    def get_move(self):
        return self.move

    def get_index(self):
        return self.index
