from BoardRep import BoardRep

class Node:


    def __init__(self, board, move_squares = None, previous_node = None, next_nodes = None):
        self.board = board
        self.next_nodes = next_nodes
        self.move_squares = move_squares

        self.score = BoardRep.getScore(board)


    def setNextNodes(self, moves):
        self.next_nodes = []
        for move in moves:
            new_node = Node(move[:][0], move[:][1], self)
            self.next_nodes.append(new_node)

