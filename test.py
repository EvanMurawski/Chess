import unittest

from BoardRep import BoardRep


class TestScore(unittest.TestCase):

    def testStartingScore(self):
        board = BoardRep()

        score = board.getScore()
        self.assertEqual(score, 0)


if __name__ == '__main__':
    unittest.main()