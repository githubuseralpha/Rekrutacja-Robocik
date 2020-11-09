from board_functions import *
from Scenario import Scenario


class Game:
    def __init__(self, board):
        self.board = board
        self.scenarios = [Scenario(board, [], "", 0)]
        self.scenarios[0].update_figures(board)

    def simulate_move(self, color):
        new_scenarios = []
        index = 0
        for scenario in self.scenarios:
            index = index + 1
            acting_figures = []

            for figure in scenario.get_figures():
                if figure.color == color:
                    acting_figures.append(figure)

            for figure in acting_figures:
                [x, y] = figure.get_position()
                possible_moves = figure.simulate_move(scenario.get_board())
                for move in possible_moves:
                    new_board = copy_board(scenario.get_board())
                    new_board[y][x] = "--"
                    new_move = (columns[x] +
                                str(8-y) +
                                '->' +
                                columns[move[0]] +
                                str(8-move[1])
                                )

                    if figure.get_type() == 'p' and (move[1] == 7 or move[1] == 0):
                        new_board[move[1]][move[0]] = (figure.get_color() +
                                                       'q'
                                                       )
                        new_scenarios.append(Scenario(new_board, [], new_move, index))
                        new_scenarios[-1].update_figures(new_board)
                        new_board[move[1]][move[0]] = (figure.get_color() +
                                                       'k'
                                                       )
                        new_scenarios.append(Scenario(new_board, [], new_move, index))
                        new_scenarios[-1].update_figures(new_board)
                    else:
                        new_board[move[1]][move[0]] = (figure.get_color() +
                                                       figure.get_type()
                                                       )
                        new_scenarios.append(Scenario(new_board, [], new_move, index))
                        new_scenarios[-1].update_figures(new_board)
            new_scenarios.append(Scenario(scenario.get_board(),
                                          scenario.get_figures(),
                                          scenario.get_move(),
                                          index))
        self.scenarios = new_scenarios.copy()

    def simulate_danger_zone(self, color):
        for scenario in self.scenarios:
            attacking_figures = []

            for figure in scenario.get_figures():
                if figure.color == color:
                    attacking_figures.append(figure)

            board = copy_board(scenario.get_board())
            for figure in attacking_figures:
                possible_moves = figure.simulate_move(board)
                if getattr(figure, "simulate_attack", False):
                    possible_moves = figure.simulate_attack(board)
                for move in possible_moves:
                    scenario.danger_board[move[1]][move[0]] = "xx"

    def check_if_mate(self, color):
        checks_in_scenarios = []
        [x_king_def, y_king_def] = [0, 0]
        [x_king_atk, y_king_atk] = [0, 0]

        for scenario in self.scenarios:
            for figure in scenario.get_figures():
                if figure.color != color and figure.type_of_piece == "W":
                    [x_king_def, y_king_def] = figure.get_position()
                if figure.color == color and figure.type_of_piece == "W":
                    [x_king_atk, y_king_atk] = figure.get_position()

            board = scenario.danger_board
            if board[y_king_def][x_king_def] == "xx" and board[y_king_atk][x_king_atk] == color + "W":
                checks_in_scenarios.append([scenario.index, True])
            else:
                checks_in_scenarios.append([scenario.index, False])

        checkmates = [i for i in range(checks_in_scenarios[-1][0])]
        for check in checks_in_scenarios:
            if check[1] is False and check[0] in checkmates:
                checkmates.remove(check[0])

        scenarios_after_one = []
        for i in range(len(self.scenarios)-1):
            if self.scenarios[i].get_index() != self.scenarios[i+1].get_index():
                scenarios_after_one.append(self.scenarios[i])

        winning_moves = []
        for scenario in scenarios_after_one:
            if scenario.get_index() in checkmates:
                winning_moves.append(scenario.get_move())
        return winning_moves
