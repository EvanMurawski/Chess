from BoardRep import BoardRep
from FENUtil import FENUtil



my_fen_board = FENUtil.fenToBoard("2r4r/p1kp1Rp1/B1p3Nn/3P3p/5B2/3P4/PPP2PPP/RN1Q2K1 b - - 2 15")
my_fen_board.print()


newBoards = my_fen_board.getLegalMoves()

for i in range(0, len(newBoards)):
    newBoards[i][0].print()
    print("\n")
    print(BoardRep.numbersToAlg(newBoards[i][1]))
    print("-------------------\n")


print(BoardRep.numbersToAlg([0, 8]))


if(BoardRep.isInCheck(my_fen_board)):
    print("check")
else:
    print("not check")


if(BoardRep.isInCheckOtherPlayer(my_fen_board)):
    print("illegal")
else:
    print("not illegal")