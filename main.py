import cv2
from show_game import ShowDisplay

def main():
    my_board = [[0, 0, 2, 0], [2, 18, 0, 0], [0, 0, 4, 0], [0, 0, 0, 4]]

    showing = ShowDisplay(my_board)
    showing.print_display()
    
    # select your choice
    while(1):
        cv2.imshow('image', showing.img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        if k == 119 or k == 115 or k == 100 or k == 97:
            #call the fuction here
 
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
