from xo import HumanPlayer, RandomComputerPlayer, XO


def main():
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = XO()
    t.play(x_player, o_player, print_game=True)


if __name__ == '__main__':
    main()