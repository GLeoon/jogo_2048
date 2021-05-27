
class ShowDisplay:

    def __init__(self, display):
        self.display = display
        self.largest = self.identify_largest()

    def identify_largest(self):
        temp_largest = self.display[0][0]
        for row in self.display:
            for colum in row:
                if colum > temp_largest:
                    temp_largest = colum
        return len(str(temp_largest))

    def print_display(self):
        for row in self.display:
            curr_row = '|'
            for pointer_positioon in row:
                if pointer_positioon == 0:
                    curr_row += ' ' * self.largest + '|'
                else:
                    curr_row += (' ' * (self.largest - len(str(pointer_positioon))
                                       )) + str(pointer_positioon) + '|'
            print(curr_row)
