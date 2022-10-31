import unittest
import pickle
from FENUtil import FENUtil


from BoardRep import BoardRep


class TestScore(unittest.TestCase):

    def testStartingScore(self):
        board = BoardRep()

        score = board.getScore()
        self.assertGreater(score, -0.2)
        self.assertLess(score, 0.2)

class TestCheckmate(unittest.TestCase):

    def testOneCheckmate(self):
        board = FENUtil.fenToBoard("rnbqkbnr/2pp1Qpp/pp6/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        self.assertTrue(board.isCheckmate())

    def testManyCheckmates(self):
        f = open('store.pck1', 'rb')
        fen_checkmates = pickle.load(f)
        f.close()

        i = 0
        j = 0
        for fen_checkmate in fen_checkmates:
            board = FENUtil.fenToBoard(fen_checkmate)
            try:
                self.assertTrue(board.isCheckmate())
                score = board.getScore()
                if board.whitemove:
                    self.assertEqual(score, -999)
                else:
                    self.assertEqual(score, 999)

            except AssertionError:
                j += 1
                print(fen_checkmate)

            i += 1

        print("Tested " + str(i) + " checkmates.")
        print(str(j) + " failed.")

    def testManyNonCheckmates(self):
        f = open('storenotcheckmate.pck1', 'rb')
        not_checkmates = pickle.load(f)
        f.close()

        i = 0
        j = 0
        for not_checkmate in not_checkmates:
            board = FENUtil.fenToBoard(not_checkmate)
            try:
                self.assertFalse(board.isCheckmate())
            except AssertionError:
                j += 1
                print(not_checkmate)

            i += 1

        print("Tested " + str(i) + " non-checkmates.")
        print(str(j) + " failed.")

if __name__ == '__main__':
    unittest.main()