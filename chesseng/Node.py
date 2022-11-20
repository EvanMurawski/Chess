from chesseng.BoardRep import BoardRep

class Node:

    numnodes = 0

    def __init__(self, board, move_squares = None, previous_node = None, next_nodes = None, best_node_idx = None):
        self.board = board
        self.next_nodes = next_nodes
        self.move_squares = move_squares
        self.best_node_idx = best_node_idx
        self.score = None
        self.previous_node = previous_node
        Node.numnodes += 1

    def setNextNodes(self, moves):
        self.next_nodes = []
        for move in moves:
            new_node = Node(move[:][0], move[:][1], self)
            self.next_nodes.append(new_node)


    def buildNextLayer(self):
        next_moves = self.board.getLegalMoves()
        self.setNextNodes(next_moves)

    def getScore(self):
        if self.score is None:
            self.score = BoardRep.getScore(self.board)
        return self.score