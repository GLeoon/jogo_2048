import cv2
from show_game import ShowDisplay
from make_move import Move
import time


def main():
    elements = [[0, 0, 2, 16], [2, 2, 0, 0], [4, 0, 4, 0], [0, 0, 0, 4]]

    showing = ShowDisplay(elements)
    press_botton = Move()

    # select your choice
    while(1):
        cv2.imshow('image', showing.img)
        k = cv2.waitKey(1) & 0xFF

        if k == 13:  # press enter to run game
            showing.print_display(elements)
        if k == 27:  # press esc to stop game
            break
        if k == 119 or k == 115 or k == 100 or k == 97:  # keys to play - w a s d
            press_botton.move(elements, k)
            showing.print_display(press_botton.new_elements)

        # time.sleep(0.5)
        # print(k)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
