from BoardRep import BoardRep
from FENUtil import FENUtil
from Tree import Tree
from Node import Node
from MiniMax import MiniMax


my_fen_board = FENUtil.fenToBoard("r1b1kbnr/pppp1ppp/2n5/4p1q1/4PP2/3P4/PPP3PP/RNBQKBNR w KQkq - 1 4")
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


root_node = Node(my_fen_board)
Tree.buildTree(root_node, 3, 0)

best_node = MiniMax.minimaxMove(root_node)
best_move = best_node.move_squares

move_string = BoardRep.numbersToAlg(best_move)
print("bestmove " + move_string)
