from show_game import ShowDisplay


def main():
    my_board = [[0, 0, 2, 0], [2, 89999, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # select your choice
    showing = ShowDisplay(my_board)
    showing.print_display()


if __name__ == "__main__":
    main()
