import unittest
from xo import XO, RandomComputerPlayer

class TestXOGame(unittest.TestCase):
    def test_make_move(self):
        game = XO()
        self.assertTrue(game.make_move(0, 'X'))
        self.assertEqual(game.board[0], 'X')
        self.assertFalse(game.make_move(0, 'O'))
        self.assertEqual(game.board[0], 'X')

    def test_winner_row(self):
        game = XO()
        game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(game.winner(1, 'X'))

    def test_winner_column(self):
        game = XO()
        game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertTrue(game.winner(3, 'X'))

    def test_winner_diagonal(self):
        game = XO()
        game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(game.winner(4, 'X'))

    def test_no_winner(self):
        game = XO()
        game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        self.assertFalse(game.winner(4, 'X'))

    def test_available_moves(self):
        game = XO()
        game.board = ['X', 'O', ' ', ' ', 'X', 'O', ' ', ' ', 'O']
        self.assertEqual(game.available_moves(), [2, 3, 6, 7])

    def test_empty_squares(self):
        game = XO()
        self.assertTrue(game.empty_squares())
        game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        self.assertFalse(game.empty_squares())

    def test_num_empty_squares(self):
        game = XO()
        self.assertEqual(game.num_empty_squares(), 9)
        game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        self.assertEqual(game.num_empty_squares(), 0)

    def test_random_player_move(self):
        game = XO()
        player = RandomComputerPlayer('X')
        move = player.get_move(game)
        self.assertIn(move, range(9))


if __name__ == '__main__':
    unittest.main()
