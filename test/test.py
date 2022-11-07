import unittest
from chesseng.FENUtil import FENUtil
import chesseng.AlphaBetaNew as AlphaBetaNew
from chesseng.Node import Node
from chesseng.BoardRep import BoardRep
import chess.pgn


class TestAlphaBeta(unittest.TestCase):

    TACTICS_FILE_NAME = "../data/tactics.txt"

    #TODO: Create more tactics to test
    def testTactics(self):
        file = open(self.TACTICS_FILE_NAME, 'r')

        num_tested = 0
        num_failed = 0
        while True:
            fen = file.readline()
            if not fen:
                break
            solution = file.readline()
            board = FENUtil.fenToBoard(fen)
            best_node = AlphaBetaNew.getBestMoveMulti(Node(board), board.whitemove)
            best_move = [best_node.board, best_node.move_squares]
            move_string = BoardRep.moveToAlg(best_move)
            try:
                self.assertEqual(move_string+"\n", solution)
            except AssertionError:
                num_failed += 1
                print("Failed tactic: ", fen)
                raise AssertionError

            num_tested += 1

        print("Tested ", num_tested , " tactics, ", num_failed , " failed.")
        file.close()

class TestBoardRep(unittest.TestCase):

    NUM_TEST_MOVE_GENERATION = 500
    PGN_FILE_NAME = "../data/20kgames.pgn"
    CHECKMATES_TEST_FILE = "../data/checkmate_test.txt"


    def testGetLegalMoves(self):
        pgn = open(self.PGN_FILE_NAME)
        num_positions = 0

        for i in range(0, self.NUM_TEST_MOVE_GENERATION):

            game = chess.pgn.read_game(pgn)
            mainline = game.mainline()

            for move in mainline:
                fen = move.board().fen()
                legals = list(move.board().legal_moves)
                num_legal = len(legals)
                legals_str = [str(move) for move in legals]

                my_boardrep = FENUtil.fenToBoard(fen)
                my_moves = my_boardrep.getLegalMoves()
                my_num_legal = len(my_moves)
                my_str = [BoardRep.moveToAlg(item) for item in my_moves]

                num_positions += 1
                try:
                    self.assertEqual(my_num_legal, num_legal)

                except AssertionError:
                    print("Error found in game number: ", i)
                    print(fen)

                    for movestring in my_str:
                        if movestring not in legals_str:
                            print("My move ", movestring, " is not in legal moves")

                    for legalmove in legals_str:
                        if legalmove not in my_str:
                            print("Legal move ", legalmove, " is not in my moves")

                    raise AssertionError

        pgn.close()
        print("Tested legal move generation for ", num_positions, " positions. ")


    def testManyCheckmates(self):
        f = open(self.CHECKMATES_TEST_FILE, 'r')

        num_tests = 0
        num_failed = 0
        num_checkmate = 0
        num_noncheckmate = 0
        while True:
            fen = f.readline()
            if not fen:
                break
            board = FENUtil.fenToBoard(fen)

            checkmate_status = f.readline()
            try:
                if checkmate_status == "True\n":
                    num_checkmate += 1
                    self.assertTrue(board.isCheckmate())
                    expected_score = -999 if board.whitemove else 999
                    self.assertEqual(board.getScore(), expected_score)
                else:
                    num_noncheckmate += 1
                    self.assertFalse(board.isCheckmate())

            except AssertionError:
                num_failed += 1
                print("Failed checkmate check in position: \n", fen)
                f.close()
                raise AssertionError

            num_tests += 1

        f.close()
        print("Checked checkmate status for ", num_tests, " positions, ", num_failed, " failed. " ,num_checkmate,
              " positions were checkmate and ", num_noncheckmate, " positions were not checkmate")


    #TODO: Test case for stalemate


if __name__ == '__main__':
    unittest.main()