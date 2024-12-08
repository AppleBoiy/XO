#!/usr/bin/env python3
import random

BOARD_SIZE = 9
ROWS = 3
EMPTY_TILE = " "


def empty_tiles(board):
    return [i for i, tile in enumerate(board) if tile == EMPTY_TILE]


def get_random_move(board, seed=None):
    if seed is not None:
        random.seed(seed)
    return random.choice(empty_tiles(board))


def check_winner(board, player):
    win_pattern = [player] * ROWS
    for i in range(ROWS):
        if board[ROWS * i:ROWS * i + ROWS] == win_pattern:
            return player
        if board[i::ROWS] == win_pattern:
            return player
    if [board[c] for c in [0, 4, 8]] == win_pattern:
        return player
    if [board[c] for c in [2, 4, 6]] == win_pattern:
        return player
    return None


def move(board, player, position):
    if board[position] != EMPTY_TILE:
        return False
    board[position] = player
    return True


def print_board(board):
    for i in range(0, BOARD_SIZE, ROWS):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
    print("-" * 5)


def play_turn(board, player, position=None, seed=None):
    if player == "O":
        move(board, player, get_random_move(board, seed))
    else:
        if position is None or not move(board, player, position):
            return False
    return True


def main():
    board = [EMPTY_TILE] * BOARD_SIZE
    current_player = random.choice(["X", "O"])
    while True:
        print(f"{current_player}'s Turn")
        print_board(board)
        if EMPTY_TILE not in board:
            print("It's a draw!")
            break
        if current_player == "O":
            play_turn(board, current_player)
        else:
            valid_move = False
            while not valid_move:
                try:
                    move_to = int(input("Get move (0-8): "))
                    valid_move = play_turn(board, current_player, move_to)
                except (ValueError, EOFError):
                    print("Invalid move or no input. Skipping...")
                    valid_move = True  # Force break to avoid infinite loop
        winner = check_winner(board, current_player)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        current_player = "X" if current_player == "O" else "O"
#if __name__ == "__main__":
#    main()

## -- End Game -- ##

import unittest

class TestTicTacToe(unittest.TestCase):
    def test_empty_tiles(self):
        board = ["X", "O", " ", " ", "X", "O", " ", " ", " "]
        self.assertEqual(empty_tiles(board), [2, 3, 6, 7, 8])

    def test_check_winner_horizontal(self):
        board = ["X", "X", "X", " ", "O", "O", " ", " ", " "]
        self.assertEqual(check_winner(board, "X"), "X")
        self.assertIsNone(check_winner(board, "O"))

    def test_check_winner_vertical(self):
        board = ["X", "O", " ", "X", "O", " ", "X", " ", " "]
        self.assertEqual(check_winner(board, "X"), "X")
        self.assertIsNone(check_winner(board, "O"))

    def test_check_winner_diagonal(self):
        board = ["X", " ", "O", " ", "X", " ", "O", " ", "X"]
        self.assertEqual(check_winner(board, "X"), "X")
        self.assertIsNone(check_winner(board, "O"))

    def test_move(self):
        board = [" ", " ", " "]
        self.assertTrue(move(board, "X", 0))
        self.assertEqual(board, ["X", " ", " "])
        self.assertFalse(move(board, "O", 0))

    def test_get_random_move(self):
        board = ["X", "O", " ", " ", "X", "O", " ", " ", " "]
        move = get_random_move(board, seed=42)
        self.assertIn(move, [2, 3, 6, 7, 8])

if __name__ == "__main__":
    unittest.main()
