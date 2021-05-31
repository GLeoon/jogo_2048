import cv2
from show_game import ShowDisplay
from make_move import Move
from check_drop_win import Drop
from creat_random import RandomNumber
# import time


def main():
    # elements = [[0, 0, 2, 16], [2, 2, 0, 0], [4, 0, 4, 8], [0, 0, 0, 4]]
    showing = ShowDisplay()

    # select your choice
    while(1):
        cv2.imshow('image', showing.img)
        k = cv2.waitKey(1) & 0xFF

        if k == 13:  # press enter to run game
            random_number = RandomNumber()
            showing.print_display(random_number.new_board)
        if k == 27:  # press esc to stop game
            break
        if k == 119 or k == 115 or k == 100 or k == 97:  # keys to play - w a s d
            press_botton = Move(random_number.new_board, k)
            after_drop = Drop(press_botton.new_elements,
                              press_botton.sum, random_number)
            showing.print_display(after_drop.elements)

        # time.sleep(0.5)
        # print(k)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
