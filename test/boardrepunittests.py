import unittest
from chesseng.FENUtil import FENUtil
from chesseng.BoardRep import BoardRep


class TestBoardRep(unittest.TestCase):


    def testNumbersToAlg(self):
        alg = BoardRep.numbersToAlg([52,36])
        self.assertEqual(alg, "e2e4")

    def testMoveToAlg(self):
        board = FENUtil.fenToBoard("3k1n2/6P1/8/8/8/8/8/4K3 w - - 0 1").getBoard(14, 5, BoardRep.WHITE_QUEEN)
        move = [board, [14, 5]]
        alg = BoardRep.moveToAlg(move)
        self.assertEqual(alg, "g7f8q")

    def testIsInCheck(self):
        board = FENUtil.fenToBoard("r1bqk1nr/pppp1Bpp/2n5/2b1p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 0 1")
        self.assertTrue(BoardRep.isInCheck(board))

    def testIsInCheckOtherPlayer(self):
        board = FENUtil.fenToBoard("r1bqk1nr/pppp1Bpp/2n5/2b1p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 1")
        self.assertTrue(BoardRep.isInCheckOtherPlayer(board))

    def testIsCheckmate(self):
        board = FENUtil.fenToBoard("rnbqkbnr/2pp1Qpp/pp6/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        self.assertTrue(board.isCheckmate())

    def testStartingScore(self):
        board = BoardRep()

        score = board.getScore()
        self.assertGreater(score, -0.2)
        self.assertLess(score, 0.2)

    def testCheckmateScore(self):
        board = FENUtil.fenToBoard("r1bqkbnr/ppp2Qpp/2np4/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        score = board.getScore()
        self.assertTrue(score, 999)

        board = FENUtil.fenToBoard("rnb1k1nr/pppp1ppp/8/2b1p3/4P3/PPP5/3P1qPP/RNBQKBNR w KQkq - 0 5")
        score = board.getScore()
        self.assertTrue(score, -999)

    def testGetWeightedMaterial(self):
        board = BoardRep()
        weighted_material = board.getWeightedMaterial()
        self.assertGreater(weighted_material, -0.2)
        self.assertLess(weighted_material, 0.2)

    def testGetMaterial(self):
        board = BoardRep()
        material = board.getMaterial()
        self.assertEqual(material, 0)

    def testGetBoard(self):
        # Basic Move
        board = BoardRep()
        new_board = board.getBoard(52,36)
        self.assertEqual(new_board.array[36], BoardRep.WHITE_PAWN)
        self.assertEqual(new_board.array[52], BoardRep.EMPTY)

        # White Castling
        board = FENUtil.fenToBoard("r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4")
        new_board = board.getBoard(60, 62)
        self.assertEqual(new_board.array[62], BoardRep.WHITE_KING)
        self.assertEqual(new_board.array[61], BoardRep.WHITE_ROOK)
        self.assertEqual(new_board.array[63], BoardRep.EMPTY)
        self.assertEqual(new_board.whitecastle, 0)

        # Black Queenside Castling
        board = FENUtil.fenToBoard("r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQ1RK1 b kq - 0 5")
        new_board = board.getBoard(4, 6)
        self.assertEqual(new_board.array[6], BoardRep.BLACK_KING)
        self.assertEqual(new_board.array[5], BoardRep.BLACK_ROOK)
        self.assertEqual(new_board.array[7], BoardRep.EMPTY)
        self.assertEqual(new_board.blackcastle, 0)

        # Castling eligibility removal
        board = FENUtil.fenToBoard("r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4")
        new_board = board.getBoard(60,52)
        self.assertEqual(new_board.whitecastle, 0)
        new_board = board.getBoard(63,62)
        self.assertEqual(new_board.whitecastle, 2)

        # En Passant
        board = FENUtil.fenToBoard("rnbqkbnr/ppp1p1pp/8/3p1pP1/8/8/PPPPPP1P/RNBQKBNR w KQkq f6 0 3")
        new_board = board.getBoard(30, 21)
        self.assertEqual(new_board.array[21], BoardRep.WHITE_PAWN)
        self.assertEqual(new_board.array[29], BoardRep.EMPTY)

    def testIsEnemyPiece(self):
        board = BoardRep()
        self.assertTrue(board.isEnemyPiece(BoardRep.BLACK_PAWN))

    def testSquareHasEnemyKing(self):
        board = BoardRep()
        self.assertTrue(board.squareHasEnemyKing(4))

    def testIsEnemyKing(self):
        board = BoardRep()
        self.assertTrue(board.isEnemyKing(BoardRep.BLACK_KING))

    def testGetPseudoLegalKingMoves(self):

        # Caslting eligibility
        board = FENUtil.fenToBoard("r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w - - 8 6")
        moves = board.getPseudoLegalKingMoves(60)
        moves_list = [moves[k][1][:] for k in range(len(moves))]
        self.assertFalse([60,62] in moves_list)
        self.assertTrue([60, 61] in moves_list)

        board = FENUtil.fenToBoard("r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/5N1P/PPPPQPP1/RNB1K2R b - - 2 7")
        moves = board.getPseudoLegalKingMoves(4)
        moves_list = [moves[k][1][:] for k in range(len(moves))]
        self.assertFalse([4, 6] in moves_list)
        self.assertTrue([4,5] in moves_list)

    def testCanKingsideCastle(self):

        # Ok to castle
        board = FENUtil.fenToBoard("rn1qk2r/pppbbppp/3p1n2/4p3/4P3/P1N2N2/1PPPBPPP/R1BQK2R w KQkq - 3 6")
        self.assertTrue(board.canKingSideCastle(60))

        board = FENUtil.fenToBoard("rnbqk2r/ppp1bppp/3p1n2/4p3/4P3/P1N2N2/1PPPBPPP/R1BQK2R b KQkq - 2 5")
        self.assertTrue(board.canKingSideCastle(4))

        # In check
        board = FENUtil.fenToBoard("r1bqk2r/pppp1ppp/2n2n2/4p3/1b2P3/3P1N2/PPP1BPPP/RNBQK2R w KQkq - 5 5")
        self.assertFalse(board.canKingSideCastle(60))

        board = FENUtil.fenToBoard("rnbqk2r/ppp1bppp/3p1n2/1B2p3/4P3/P1N2N2/1PPP1PPP/R1BQK2R b KQkq - 2 5")
        self.assertFalse(board.canKingSideCastle(4))

        # Passthru square attacked
        board = FENUtil.fenToBoard("rn1qkbnr/ppp2ppp/3p4/4p3/4P3/PP1b1N2/2PP1PPP/RNBQK2R w KQkq - 0 6")
        self.assertFalse(board.canKingSideCastle(60))

        board = FENUtil.fenToBoard("rnbqk2r/pppp1ppp/5n2/4p3/1B2P3/3P4/PPP2PPP/RN1QKBNR b KQkq - 0 4")
        self.assertFalse(board.canKingSideCastle(4))

        # Rook attacked
        board = FENUtil.fenToBoard("rn1qkb1r/pbpp1ppp/1p3n2/4p3/2B5/4P1P1/PPPPNP1P/RNBQK2R w KQkq - 2 5")
        self.assertTrue(board.canKingSideCastle(60))

        board = FENUtil.fenToBoard("rnbqk2r/ppppnp1p/4p1p1/2b5/8/1P2PN2/PBPPBPPP/RN1QK2R b KQkq - 4 5")
        self.assertTrue(board.canKingSideCastle(4))

        # Piece in between
        board = FENUtil.fenToBoard("rnbqk1nr/pppp1ppp/8/2b1p3/2B1P3/8/PPPP1PPP/RNBQK1NR w KQkq - 2 3")
        self.assertFalse(board.canKingSideCastle(60))

        board = FENUtil.fenToBoard("rnbqk1nr/pppp1ppp/8/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3")
        self.assertFalse(board.canKingSideCastle(4))

    def testCanQueensideCastle(self):

        # Ok to castle
        board = FENUtil.fenToBoard("r3kbnr/pppbqppp/2np4/4p3/4P3/2NP4/PPPBQPPP/R3KBNR w KQkq - 4 6")
        self.assertTrue(board.canQueenSideCastle(60))

        board = FENUtil.fenToBoard("r3kbnr/pppbqppp/2np4/4p3/4P3/2NP4/PPPBQPPP/2KR1BNR b kq - 5 6")
        self.assertTrue(board.canQueenSideCastle(4))

        # In Check
        board = FENUtil.fenToBoard("rnb1kbnr/pppp2pp/5p2/4p3/1q2P3/N2PB3/PPP1QPPP/R3KBNR w KQkq - 2 6")
        self.assertFalse(board.canQueenSideCastle(60))

        board = FENUtil.fenToBoard("r3kbnr/ppp1qppp/n2p4/1Q2pb2/4P3/2N2P1N/PPPP2PP/R1B1KB1R b KQkq - 5 6")
        self.assertFalse(board.canQueenSideCastle(4))

        # Passthru square attacked
        board = FENUtil.fenToBoard("r3k1nr/ppp1pp1p/n1qpB1pb/8/8/N1QP1NP1/PPPBPP1P/R3K2R b KQkq - 0 9")
        self.assertFalse(board.canQueenSideCastle(4))

        board = FENUtil.fenToBoard("rn2k1nr/ppp1pp1p/2qp2p1/5b2/5b2/N1QP2PB/PPP1PP1P/R3K1NR w KQkq - 0 8")
        self.assertFalse(board.canQueenSideCastle(60))

        board = FENUtil.fenToBoard("r3kbnr/p1pp1ppp/np2pq2/8/8/NP2Pb1P/PBPP1PP1/R3KBNR w KQkq - 0 7")
        self.assertFalse(board.canQueenSideCastle(60))

        board = FENUtil.fenToBoard("r3kbnr/pbpp1ppp/np2pB2/8/8/NP2PQ2/P1PP1PPP/R3KBNR b KQkq - 0 6")
        self.assertFalse(board.canQueenSideCastle(4))

        # Rook passthru square attacked
        board = FENUtil.fenToBoard("r3kbnr/pb2pppp/nppp4/5q2/3P4/NPP5/PB1QPPPP/R3KBNR w KQkq - 1 8")
        self.assertTrue(board.canQueenSideCastle(60))

        board = FENUtil.fenToBoard("r3kbnr/pb2pppp/npp5/3p1q2/3P1Q2/NPP2N2/PB2PPPP/R3KB1R b KQkq - 1 9")
        self.assertTrue(board.canQueenSideCastle(4))

        # Rook attacked
        board = FENUtil.fenToBoard("r3k1nr/p1pbppbp/np1pq1p1/8/8/NP1PQ1P1/P1PBPPBP/R3K1NR w KQkq - 6 9")
        self.assertTrue(board.canQueenSideCastle(60))

        board = FENUtil.fenToBoard("r3k1nr/p1pbppbp/np1pq1p1/8/8/NP1PQ1P1/P1PBPPBP/2KR2NR b kq - 7 9")
        self.assertTrue(board.canQueenSideCastle(4))

        # Piece in between
        board = FENUtil.fenToBoard("rn2k1nr/pbpqppbp/1p1p2p1/8/8/1P1P2P1/PBPQPPBP/RN2K1NR w KQkq - 2 7")
        self.assertFalse(board.canQueenSideCastle(60))

        board = FENUtil.fenToBoard("rn2k1nr/pbpqppbp/1p1p2p1/8/8/1P1P1NP1/PBPQPPBP/RN2K2R b KQkq - 3 7")
        self.assertFalse(board.canQueenSideCastle(4))

    # TODO: Test cases for specific edge cases


if __name__ == '__main__':
    unittest.main()