

class Drop():
    def __init__(self, elements, was_sum, random_number):
        self.was_sum = was_sum
        self.elements = elements
        self.random = random_number
        self.chek_win_or_loose()
        if self.was_sum == False:
            self.random.raffler_points(1)

    def chek_win_or_loose(self):
        for i in range(len(self.elements)):
            for j in range(len(self.elements)):
                if self.elements[i][j] == 0:
                    pass
                if self.elements[i][j] == 2048:
                    pass
