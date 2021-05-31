import random


class RandomNumber():

    def __init__(self):
        self.new_board = None
        self.pick_new_board()
        self.raffler_points(2)

    def pick_new_board(self):
        tem_board = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(0)
            tem_board.append(row)
        self.new_board = tem_board

    def raffler_num(self):
        if random.randint(0, 6) == 1:
            return 4
        else:
            return 2

    def raffler_points(self, number_of_spots):
        while number_of_spots > 0:
            row_num = random.randint(0, 3)
            colum_num = random.randint(0, 3)

            if self.new_board[row_num][colum_num] == 0:
                self.new_board[row_num][colum_num] = self.raffler_num()
                number_of_spots -= 1
