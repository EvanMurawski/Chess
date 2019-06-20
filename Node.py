from BoardRep import BoardRep

class Node:


    def __init__(self, board, previous_node = None, next_nodes = None):
        self.board = board
        self.next_nodes = next_nodes

        self.score = BoardRep.getScore(board)


    def setNextNodes(self, moves):
        for move in moves:
            new_node = Node(move[:][0], self)
            self.next_nodes.extend(new_node)

