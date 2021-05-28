class Move:
    def __init__(self,elements, direction):
        self.old_elements = elements
        self.direction=direction
        self.new_elements = []
        self.sum = False
        self.move()

    def move(self):

        if self.direction == 115:
            print('baixo')
            self.move_down()
        if self.direction == 119:
            print('cima')
            self.move_up()
        if self.direction == 100:
            print('direita')
            self.move_right(self.old_elements)
        if self.direction == 97:
            print('esquerda')
            self.move_left(self.old_elements)

    def move_down(self):
        row = self.transpose(self.old_elements)
        self.move_right(row)
        row = self.transpose(self.new_elements)
        self.new_elements = row

    def move_up(self):
        row = self.transpose(self.old_elements)
        self.move_left(row)
        row = self.transpose(self.new_elements)
        self.new_elements = row

    def move_right(self, elements):

        for i in range(len(self.old_elements)):
            elements[i] = self.reverse(elements[i])

        self.move_left(elements)

        for i in range(len(self.old_elements)):
            elements[i] = self.reverse(elements[i])
        self.new_elements=elements

    def move_left(self,elements):
        for i in range(len(self.old_elements)):
            row = self.make_move_side(elements[i])
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
                self.sum = True
        return row

    def reverse(self, row):
        # reversed
        temp = []
        for i in range(len(self.old_elements)-1, -1, -1):
            temp.append(row[i])
        return temp

    def transpose(self, row):
        # trasnpose
        temp = []
        for j in range(len(self.old_elements)):
            for i in range(j, len(self.old_elements)):
                if i != j:
                    temp = row[j][i]
                    row[j][i] = row[i][j]
                    row[i][j] = temp
        return row


        
            # row = self.make_move_side(self.old_elements[i])
            # row = self.check_number_equal_side(row)
            # row = self.make_move_side(row)
            # self.new_elements.append(row)
