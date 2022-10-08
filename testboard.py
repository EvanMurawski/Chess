from BoardRep import BoardRep
from FENUtil import FENUtil
from Tree import Tree
from Node import Node
from MiniMax import MiniMax
from AlphaBetaNew import AlphaBetaNew
import time

my_fen_board = FENUtil.fenToBoard("rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
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


# if(BoardRep.isInCheckOtherPlayer(my_fen_board)):
#     print("illegal")
# else:
#     print("not illegal")

if(my_fen_board.isCheckmate()):
    print("checkmate")
else:
    print("not checkmate")

print(str(my_fen_board.getScore()))

root_node = Node(my_fen_board)

start_time = time.time()
best_node = AlphaBetaNew.getBestMoveWhite(root_node, 5)
best_move = best_node.move_squares
print("elapsed time: " + str(time.time() - start_time) + "\n\n")

move_string = BoardRep.numbersToAlg(best_move)
print("bestmove " + move_string)

print("number nodes: " + str(Node.numnodes))
print("number boards: " + str(BoardRep.numboards))
print("num getcheck " + str(BoardRep.numgetcheck) + "time: " + str(BoardRep.getchecktime))
print("num getothercheck " + str(BoardRep.numgetothercheck)+ "time: " + str(BoardRep.getotherchecktime))
print("num getcheckmate " + str(BoardRep.numgetcheckmate)+ "time: " + str(BoardRep.getcheckmatetime))
print("num getpseudo" + str(BoardRep.numgetpseudo) + "time: " + str(BoardRep.getpseudolegaltime))
print("num getpseudocaptures" + str(BoardRep.numgetpseudocaptures) + "time " + str(BoardRep.getpseudocapturestime))
print("num getlegal " + str(BoardRep.numgetlegal) + "time: " + str(BoardRep.getlegalmovestime))


# node_to_consider = best_node
# best_node_idx = node_to_consider.best_node_idx
# while best_node_idx is not None:
#     best_next_node = node_to_consider.next_nodes[node_to_consider.best_node_idx]
#     print("Next Move: ")
#     print(BoardRep.numbersToAlg(best_next_node.move_squares))
#     print("Score: ")
#     print(str(best_next_node.score) + "\n")
#     node_to_consider = best_next_node
#     best_node_idx = node_to_consider.best_node_idx
