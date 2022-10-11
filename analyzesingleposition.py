from BoardRep import BoardRep
from FENUtil import FENUtil
from Tree import Tree
from Node import Node
from MiniMax import MiniMax
import AlphaBetaNew
import time


if __name__ == "__main__":

    #Configuration
    #-------------------
    depth = 3
    multithreading = False
    #-------------------


    my_fen_board = FENUtil.fenToBoard("rnb1kbnr/pppp1ppp/8/4p1q1/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3")
    my_fen_board.print()

    newBoards = my_fen_board.getLegalMoves()

    print("\nLegal Moves: \n")

    for i in range(0, len(newBoards)):
        newBoards[i][0].print()
        print("\n")
        print(BoardRep.numbersToAlg(newBoards[i][1]))
        print("-------------------\n")


    if(BoardRep.isInCheck(my_fen_board)):
        print("check")
    else:
        print("not check")

    if(my_fen_board.isCheckmate()):
        print("checkmate")
    else:
        print("not checkmate")

    print("Eval: ")
    print(str(my_fen_board.getScore()))

    root_node = Node(my_fen_board)

    start_time = time.time()

    if multithreading:
        best_node = AlphaBetaNew.getBestMoveMulti(root_node, my_fen_board.whitemove)
    else:
        best_node = AlphaBetaNew.getBestMoveSingle(root_node, depth, my_fen_board.whitemove)


    best_move = best_node.move_squares
    move_string = BoardRep.numbersToAlg(best_move)

    print("\nElapsed time: " + str(time.time() - start_time))
    print("Best move: " + move_string)
    print("Best move eval: " + str(best_node.score))
    print("Nodes created: " + str(Node.numnodes))
    print("Boards created: : " + str(BoardRep.numboards))
    print("num getcheck: " + str(BoardRep.numgetcheck) + " time: " + str(BoardRep.getchecktime))
    print("num getothercheck: " + str(BoardRep.numgetothercheck)+ " time: " + str(BoardRep.getotherchecktime))
    print("num getcheckmate: " + str(BoardRep.numgetcheckmate)+ " time: " + str(BoardRep.getcheckmatetime))
    print("num getpseudo: " + str(BoardRep.numgetpseudo) + " time: " + str(BoardRep.getpseudolegaltime))
    print("num getpseudocaptures: " + str(BoardRep.numgetpseudocaptures) + " time:  " + str(BoardRep.getpseudocapturestime))
    print("num getlegal: " + str(BoardRep.numgetlegal) + " time: " + str(BoardRep.getlegalmovestime))



