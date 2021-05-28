import cv2
import numpy as np


class ShowDisplay:

    def __init__(self, board):
        self.board = board
        self.largest = None
        self.img = np.zeros((400, 420, 3), np.uint8)
        self._font = cv2.FONT_HERSHEY_PLAIN

    def print_display(self, new_board):
        self.board = new_board
        self.identify_largest()
        count = 1
        for row in self.board:
            curr_row = '|'
            for pointer_positioon in row:
                if pointer_positioon == 0:
                    curr_row += ' ' * self.largest + '|'
                else:
                    curr_row += (' ' * (self.largest - len(str(pointer_positioon))
                                        )) + str(pointer_positioon) + '|'
            print(curr_row)
            cv2.putText(self.img, curr_row, (10, 70*count),
                        self._font, 2, (255, 255, 255), 2, cv2.FILLED)
            count += 1

    def identify_largest(self):
        temp_largest = 0
        for row in self.board:
            for colum in row:
                if colum > temp_largest:
                    temp_largest = colum
        self.largest = len(str(temp_largest))
