from BoardRep import BoardRep

class Node:


    def __init__(self, board, move_squares = None, previous_node = None, next_nodes = None, best_node_idx = None):
        self.board = board
        self.next_nodes = next_nodes
        self.move_squares = move_squares

        self.score = BoardRep.getScore(board)
        self.best_node_idx = best_node_idx


    def setNextNodes(self, moves):
        self.next_nodes = []
        for move in moves:
            new_node = Node(move[:][0], move[:][1], self)
            self.next_nodes.append(new_node)

