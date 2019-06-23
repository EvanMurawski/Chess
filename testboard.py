from BoardRep import BoardRep
from FENUtil import FENUtil
from Tree import Tree
from Node import Node
from MiniMax import MiniMax
from AlphaBeta import AlphaBeta


my_fen_board = FENUtil.fenToBoard("r1bqkbnr/pppppppp/n7/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2")
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

best_node = AlphaBeta.alphabetaMove(root_node, 3)
best_move = best_node.move_squares

move_string = BoardRep.numbersToAlg(best_move)
print("bestmove " + move_string)

print("number nodes: " + str(Node.numnodes))
print("number boards: " + str(BoardRep.numboards))
print("num getcheck " + str(BoardRep.numgetcheck))
print("num getothercheck " + str(BoardRep.numgetothercheck))
print("num getcheckmate " + str(BoardRep.numgetcheckmate))
print("num getpseudo" + str(BoardRep.numgetpseudo))
print("num getlegal " + str(BoardRep.numgetlegal))



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
