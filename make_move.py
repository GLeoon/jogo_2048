class Move:
    def __init__(self):
        self.old_elements = []
        self.new_elements = None

    def move(self, old_elements, direction):
        self.old_elements = old_elements
        self.new_elements = []

        if direction == 119:
            print('w')
        if direction == 115:
            print('s')
        if direction == 100:
            print('direita')
            self.move_righ()
        if direction == 97:
            print('esquerda')
            self.move_left()

    def move_righ(self):

        for i in range(len(self.old_elements)):
            self.old_elements[i] = self.reverse(self.old_elements[i])

            row = self.make_move_side(self.old_elements[i])
            row = self.check_number_equal_side(row)
            row = self.make_move_side(row)
            self.new_elements.append(row)

            self.new_elements[i] = self.reverse(self.new_elements[i])

    def move_left(self):
        for i in range(len(self.old_elements)):
            row = self.make_move_side(self.old_elements[i])
            row = self.check_number_equal_side(row)
            row = self.make_move_side(row)
            self.new_elements.append(row)

    def make_move_side(self, row):
        for i in range(len(self.old_elements) - 1):
            for i in range(len(self.old_elements)-1, 0, -1):
                if row[i-1] == 0:
                    row[i-1] = row[i]
                    row[i] = 0
        return row

    def check_number_equal_side(self, row):
        for i in range(len(self.old_elements) - 1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0
        return row

    def reverse(self, row):
        # reversed
        temp = []
        for i in range(len(self.old_elements)-1, -1, -1):
            temp.append(row[i])
        return temp

    # def transpose():
    #     # trasnpose
    #     temp = []
    #     for j in range(len(self.old_elements)):
    #         for i in range(j, len(self.old_elements)):
    #             if i != j:
    #                 temp = row[j][i]
    #                 row[j][i] = row[i][j]
    #                 row[i][j] = temp
    #     return row
