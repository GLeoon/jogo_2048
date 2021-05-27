class Move:
    def __init__(self, board, direction):
        self.board = board
        self.direction = direction

    def make_move(self):
        for row in self.board:
            for colum in row: