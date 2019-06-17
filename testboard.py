from BoardRep import BoardRep
from FENUtil import FENUtil



my_fen_board = FENUtil.fenToBoard("r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3")
my_fen_board.print()


newBoards = my_fen_board.getPseudoLegalMoves()

for i in range(0, len(newBoards)):
    newBoards[i][0].print()
    print("\n")
    print(BoardRep.numbersToAlg(newBoards[i][1]))
    print("-------------------\n")


print(BoardRep.numbersToAlg([0, 8]))