class Figure:
    def __init__(self, x, y, color, type_of_piece):
        self.x = x
        self.y = y
        self.color = color
        self.type_of_piece = type_of_piece

    def get_position(self):
        return [self.x, self.y]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type_of_piece

    def move_right(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        while x < 7:
            x += 1
            if board[y][x] == "--":
                possible_moves.append((x, y))
            elif board[y][x][0] != self.color:
                possible_moves.append((x, y))
                x = 8
            else:
                x = 8
        return possible_moves

    def move_left(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        while x > 0:
            x -= 1
            if board[y][x] == "--":
                possible_moves.append((x, y))
            elif board[y][x][0] != self.color:
                possible_moves.append((x, y))
                x = 0
            else:
                x = 0
        return possible_moves

    def move_down(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        while y < 7:
            y += 1
            if board[y][x] == "--":
                possible_moves.append((x, y))
            elif board[y][x][0] != self.color:
                possible_moves.append((x, y))
                y = 8
            else:
                y = 8
        return possible_moves

    def move_up(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        while y > 0:
            y -= 1
            if board[y][x] == "--":
                possible_moves.append((x, y))
            elif board[y][x][0] != self.color:
                possible_moves.append((x, y))
                y = 0
            else:
                y = 0
        return possible_moves

    def move_down_right(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        while y < 7 and x < 7:
            y += 1
            x += 1
            if board[y][x] == "--":
                possible_moves.append((x, y))
            elif board[y][x][0] != self.color:
                possible_moves.append((x, y))
                y = 8
            else:
                y = 8
        return possible_moves

    def move_up_right(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        while y > 0 and x < 7:
            y -= 1
            x += 1
            if board[y][x] == "--":
                possible_moves.append((x, y))
            elif board[y][x][0] != self.color:
                possible_moves.append((x, y))
                y = 0
            else:
                y = 0
        return possible_moves

    def move_up_left(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        while y > 0 and x > 0:
            y -= 1
            x -= 1
            if board[y][x] == "--":
                possible_moves.append((x, y))
            elif board[y][x][0] != self.color:
                possible_moves.append((x, y))
                y = 0
            else:
                y = 0
        return possible_moves

    def move_down_left(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        while y < 7 and x > 0:
            y += 1
            x -= 1
            if board[y][x] == "--":
                possible_moves.append((x, y))
            elif board[y][x][0] != self.color:
                possible_moves.append((x, y))
                y = 8
            else:
                y = 8
        return possible_moves

    def move_up_by_one(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if y > 0:
            if board[y-1][x] == '--':
                possible_moves.append((x, y-1))
        return possible_moves

    def move_up_by_two(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if board[y-1][x] == '--' and board[y-2][x] == '--':
            possible_moves.append((x, y-2))
        return possible_moves

    def move_up_right_by_one(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if y > 0 and x < 7:
            if board[y-1][x+1][0] != self.color and board[y-1][x+1] != '--':
                possible_moves.append((x+1, y-1))
        return possible_moves

    def move_up_left_by_one(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if y > 0 and x > 0:
            if board[y-1][x-1][0] != self.color and board[y-1][x-1] != '--':
                possible_moves.append((x-1, y-1))
        return possible_moves

    def move_down_by_one(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if y < 7:
            if board[y+1][x] == '--':
                possible_moves.append((x, y+1))
        return possible_moves

    def move_down_by_two(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if board[y+1][x] == '--' and board[y+2][x] == '--':
            possible_moves.append((x, y+2))
        return possible_moves

    def move_down_right_by_one(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if y < 7 and x < 7:
            if board[y+1][x+1][0] != self.color and board[y+1][x+1] != '--':
                possible_moves.append((x+1, y+1))
        return possible_moves

    def move_down_left_by_one(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if y < 7 and x > 0:
            if board[y+1][x-1][0] != self.color and board[y+1][x-1] != '--':
                possible_moves.append((x-1, y+1))
        return possible_moves

    def move_like_knight(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if x <= 5 and y <= 6:
            if board[y+1][x+2][0] != self.color:
                possible_moves.append((x+2, y+1))
        if x <= 6 and y <= 5:
            if board[y+2][x+1][0] != self.color:
                possible_moves.append((x+1, y+2))
        if x <= 5 and y >= 1:
            if board[y-1][x+2][0] != self.color:
                possible_moves.append((x+2, y-1))
        if x <= 6 and y >= 2:
            if board[y-2][x+1][0] != self.color:
                possible_moves.append((x+1, y-2))
        if x >= 1 and y >= 2:
            if board[y-2][x-1][0] != self.color:
                possible_moves.append((x-1, y-2))
        if x >= 2 and y >= 1:
            if board[y-1][x-2][0] != self.color:
                possible_moves.append((x-2, y-1))
        if x >= 2 and y <= 6:
            if board[y+1][x-2][0] != self.color:
                possible_moves.append((x-2, y+1))
        if x >= 1 and y <= 5:
            if board[y+2][x-1][0] != self.color:
                possible_moves.append((x-1, y+2))
        return possible_moves

    def move_by_one(self, board):
        possible_moves = []
        [x, y] = self.get_position()
        if x < 7:
            if board[y][x+1][0] != self.color:
                possible_moves.append((x+1, y))
        if y < 7:
            if board[y+1][x][0] != self.color:
                possible_moves.append((x, y+1))
        if x > 0:
            if board[y][x-1][0] != self.color:
                possible_moves.append((x-1, y))
        if y > 0:
            if board[y-1][x][0] != self.color:
                possible_moves.append((x, y-1))
        if x < 7 and y < 7:
            if board[y+1][x+1][0] != self.color:
                possible_moves.append((x+1, y+1))
        if x > 0 and y < 7:
            if board[y+1][x-1][0] != self.color:
                possible_moves.append((x-1, y+1))
        if x < 7 and y > 0:
            if board[y-1][x+1][0] != self.color:
                possible_moves.append((x+1, y-1))
        if x > 0 and y > 0:
            if board[y-1][x-1][0] != self.color:
                possible_moves.append((x-1, y-1))
        return possible_moves
