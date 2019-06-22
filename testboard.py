from BoardRep import BoardRep
from FENUtil import FENUtil
from Tree import Tree
from Node import Node
from MiniMax import MiniMax


my_fen_board = FENUtil.fenToBoard("8/8/8/1kp4R/1n6/p7/8/1K4r1 w - - 2 79")
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

if(my_fen_board.isCheckmate()):
    print("checkmate")
else:
    print("not checkmate")

print(str(my_fen_board.getScore()))

# root_node = Node(my_fen_board)
# Tree.buildTree(root_node, 3, 0)
#
# best_node = MiniMax.minimaxMove(root_node)
# best_move = best_node.move_squares
#
# move_string = BoardRep.numbersToAlg(best_move)
# print("bestmove " + move_string)
#
#
#
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
