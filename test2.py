import unittest
import main

class TestGuessGain(unittest.TestCase):

    def test_guess_game(self):
        user_num = 5
        answer = 5
        result = main.guess_game(user_num, answer)
        self.assertTrue(result)

    def test_guess_game1(self):
        user_num = 2
        answer = 5
        result = main.guess_game(user_num, answer)
        self.assertFalse(result)

    def test_guess_game2(self):
        user_num = 15
        answer = 5
        result = main.guess_game(user_num, answer)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()