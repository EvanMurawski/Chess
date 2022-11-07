from chesseng.FENUtil import FENUtil
import time
import chesseng.AlphaBetaNew as AlphaBetaNew
from chesseng.Node import Node

OPENING_POSITION = "rn1qkb1r/pp3ppp/2p1pn2/3p1b2/2PP4/5NP1/PP2PPBP/RNBQK2R w KQkq - 0 6"
MIDDLEGAME_POSITION = "rr4k1/p2nbpp1/2p1p2p/3p1b2/N2PnB2/1P3NP1/1P2PP1P/R1R2BK1 b - - 6 17"
ENDGAME_POSITION = "8/7P/5b2/8/1p6/2pK1p2/P5k1/8 w - - 3 47"

NUM_LEGAL_MOVES_TESTS = 500
NUM_MULTI_TESTS = 3
NUM_SINGLE_TESTS = 1


class PerformanceTest:

    def __init__(self):
        self.legal_move_time = 0
        self.multi_time = 0
        self.single_time = 0

    def genBoards(self):
        self.opening_board = FENUtil.fenToBoard(OPENING_POSITION)
        self.middle_board = FENUtil.fenToBoard(MIDDLEGAME_POSITION)
        self.end_board = FENUtil.fenToBoard(ENDGAME_POSITION)

    def testLegalMoveTime(self):

        for i in range(NUM_LEGAL_MOVES_TESTS):

            self.genBoards()

            start_time = time.time()
            self.opening_board.getLegalMoves()
            self.middle_board.getLegalMoves()
            self.end_board.getLegalMoves()
            end_time = time.time()

            self.legal_move_time += (end_time - start_time)

    def testMultiPerformance(self):

        for i in range(NUM_MULTI_TESTS):
            self.genBoards()
            start_time = time.time()
            AlphaBetaNew.getBestMoveMulti(Node(self.opening_board), self.opening_board.whitemove)
            AlphaBetaNew.getBestMoveMulti(Node(self.middle_board), self.middle_board.whitemove)
            AlphaBetaNew.getBestMoveMulti(Node(self.end_board), self.end_board.whitemove)
            end_time = time.time()
        self.multi_time += (end_time - start_time)

    def testSinglePerformance(self):

        for i in range(NUM_SINGLE_TESTS):
            self.genBoards()
            start_time = time.time()
            AlphaBetaNew.getBestMoveSingle(Node(self.opening_board),3, self.opening_board.whitemove)
            AlphaBetaNew.getBestMoveSingle(Node(self.middle_board), 3, self.middle_board.whitemove)
            AlphaBetaNew.getBestMoveSingle(Node(self.end_board), 3, self.end_board.whitemove)
            end_time = time.time()
        self.single_time += (end_time - start_time)


if __name__ == "__main__":

    pt = PerformanceTest()

    pt.testLegalMoveTime()
    pt.testMultiPerformance()
    pt.testSinglePerformance()

    legal_move_time_ms = pt.legal_move_time * 1000 / (NUM_LEGAL_MOVES_TESTS * 3)
    multi_move_time = pt.multi_time / (NUM_MULTI_TESTS * 3)
    single_move_time = pt.single_time / (NUM_SINGLE_TESTS * 3)


    print("Average legal move generation time (ms): ")
    print("%1.2f" % legal_move_time_ms)

    print("Average multithreaded search time (s): ")
    print("%1.2f" % multi_move_time)

    print("Average singlethreaded search time (s): ")
    print("%1.2f" % single_move_time)
