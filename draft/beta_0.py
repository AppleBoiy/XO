#!/usr/bin/env python3
import random



def empty_tile(board):
    tiles = []
    for i, t in enumerate(board):
        if t == " ":
            tiles.append(i)
    return tiles


def get_random_move(board):
    return random.choice(empty_tile(board))


def check_winner(_board, _curr_player):
    print_board(_board)
    win_pattern = [_curr_player] * 3
    for i in range(3):
        # horizontal
        horizontal = _board[3 * i: 3 * i + 3]
        if horizontal == win_pattern:
            return _curr_player
        # vertical
        if _board[i::3] == win_pattern:
            return _curr_player

    # tilted_left
    tilted_left = [_board[c] for c in [0, 4, 8]]
    if tilted_left == win_pattern:
        return _curr_player

    # tilted_right
    tilted_right = [_board[c] for c in [2, 4, 6]]
    if tilted_right == win_pattern:
        return _curr_player

    return None


def move(board, player, position):
    if board[position] != " ":
        return False
    board[position] = player
    return True


def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")


def main():
    board = [" "] * 9
    curr_player = random.choice(["X", "O"])
    while True:
        print(f"{curr_player}'s Turn")
        if curr_player == "O":
            move(board, curr_player, get_random_move(board))
        else:
            valid_move = False
            while not valid_move:
                move_to = int(input("Get move: "))
                valid_move = move(board, curr_player, move_to)
                if not valid_move:
                    print("your move is not valid!")

        print_board(board)
        winner = check_winner(board, curr_player)
        if winner:
            print(f"{winner} win!")
            break
        curr_player = "X" if curr_player == "O" else "O"


# if __name__ == "__main__":
#     main()

## -- end -- ##

import unittest
from unittest.mock import patch

class TestTicTacToe(unittest.TestCase):



    def test_empty_tile(self):
        board = [" "] * 9
        self.assertEqual(empty_tile(board), list(range(9)))
        board[0] = "X"
        self.assertEqual(empty_tile(board), list(range(1, 9)))

    def test_move_valid(self):
        board = [" "] * 9
        self.assertTrue(move(board,"X", 0))
        self.assertEqual(board[0], "X")
        self.assertFalse(move(board, "O", 0))  # Can't move to an occupied tile

    def test_check_winner_horizontal(self):
        board = [" "] * 9
        board[0] = board[1] = board[2] = "X"
        curr_player = "X"
        self.assertEqual(check_winner(board, curr_player), "X")

    def test_check_winner_vertical(self):
        board = [" "] * 9
        board[0] = board[3] = board[6] = "O"
        curr_player = "O"
        self.assertEqual(check_winner(board, curr_player), "O")

    def test_check_winner_tilted_left(self):
        board = [" "] * 9
        board[0] = board[4] = board[8] = "X"
        curr_player = "X"
        self.assertEqual(check_winner(board, curr_player), "X")

    def test_check_winner_tilted_right(self):
        board = [" "] * 9
        board[2] = board[4] = board[6] = "O"
        curr_player = "O"
        self.assertEqual(check_winner(board, curr_player), "O")

    def test_no_winner(self):
        board = [" "] * 9
        board[0] = board[1] = "X"
        curr_player = "X"
        self.assertIsNone(check_winner(board, curr_player))

    @patch("builtins.input", side_effect=[0, 1, 2])
    @patch("random.choice", side_effect=["X"])
    def test_game_simulation(self, mock_input, mock_random):
        board = [" "] * 9
        curr_player = "X"
        move(board, "X", 0)
        move(board, "X", 1)
        move(board, "X", 2)
        self.assertEqual(check_winner(board, curr_player), "X")


if __name__ == "__main__":
    unittest.main()
