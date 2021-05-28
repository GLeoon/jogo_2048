class Drop():
    def __init__(self, elements ,was_sum):
        self.was_sum= was_sum
        self.elements=elements
        self.status = 0
        self.chek_win()
        self.chek_loose()
        if status == 0:
            self.chek_drop()

    def chek_win(self):
        for i in range(len(self.elements)):
            for j in range(len(self.elements)):
                if self.elements[i][j] == 2048:
                    return 1 #do something visual to win

    def chek_loose(self):
        for i in range(len(self.elements)):
            for j in range(len(self.elements)):
                if self.elements[i][j] == 0:
                    return -1#do something visual to loose

    def chek_drop(self):
        #if some value is 0 continue
        pass