import multiprocessing
import chesseng.Node as Node

DEPTH_INITIAL = 3
DEPTH_FINAL = 5
SECONDARY_NODE_QTY = 3
SECONDARY_SEARCH = True
NUM_PROCESSES = 16


class AlphaBeta:

    def __init__(self, last_hash_map=None, multithreading=None):
        if last_hash_map is None:
            self.last_hash_map = {}
        else:
            self.last_hash_map = last_hash_map

        self.hash_map = {}

        if multithreading is None:
            self.multithreading = False
        else:
            self.multithreading = multithreading

    # TODO improve this, e.g. prioritize captures of higher value pieces, maybe consider heuristic value of the node
    def nodeSort(self, node):

        board = node.board
        key =tuple (board.array) + (board.whitemove, board.whitecastle, board.blackcastle,board.enpassant_square)

        #First check if there is already a score computed. If so, return this as the sorting value.
        if key in self.last_hash_map:
            score, _ = self.last_hash_map[key]
            return score

        # Not in hash map, use heuristics

        # Need to multiply the score by -1 if minimizing player just moved
        factor = -1 if node.board.whitemove else 1

        if board.isInCheck():
            return 0.7 * factor

        if board.is_capture:
            return 0.5 * factor

        # Black just moved, see if it is a forward move
        # From square is a lower row number -> is a forward move
        if board.whitemove and node.move_squares[0] // 8 < node.move_squares[1] // 8:
            return 0.3 * factor

        # White just moved, see if it is a forward move
        # From square is a higher row number -> is a forward move
        if (not board.whitemove) and node.move_squares[0] // 8 > node.move_squares[1] // 8:
            return 0.3 * factor

        return 0

    def abSearchMulti(self, inputs):
        return self.abSearch(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4])

    def abSearch(self, node, depth, alpha, beta, maximizingplayer):

        if depth == 0:
            return node.getScore(), []

        if node.next_nodes is None:
            node.buildNextLayer()

        if not node.next_nodes:
            return node.board.getScoreNoMoves(), []

        if maximizingplayer:
            value = -99999
            next_nodes = node.next_nodes
            #Sort in descending order, we want to check the highest scoring nodes for maximizing player
            next_nodes.sort(key = self.nodeSort, reverse= True)
            line = []

            # If we are in the first layer, multithreading will be true, spawn processes
            if self.multithreading:

                #No need to check if nodes are already in hash map, we are on the first layer
                inputs = []
                for node in next_nodes:
                    inputs.append([node]+ [depth-1, alpha, beta, False])
                pool = multiprocessing.Pool(processes=NUM_PROCESSES)
                # make a new object, pass the last hash map, set it to be single-threaded
                ab = AlphaBeta(self.last_hash_map, False)
                results = pool.map(ab.abSearchMulti, inputs)

                #TODO: find best node, add all nodes to hash map
                sorted_results = sorted(zip(inputs, results), key=lambda x: x[1][0], reverse=True)

                for result in sorted_results:
                    childnode = result[0][0]
                    key = tuple(childnode.board.array) + (childnode.board.whitemove, childnode.board.whitecastle, childnode.board.blackcastle,childnode.board.enpassant_square)
                    if not (key in self.hash_map):
                        self.hash_map[key] = (result[1][0], result[1][0])

                line = [sorted_results[0][0][0]]
                line.extend(sorted_results[0][1][1])
                return sorted_results[0][1][0], line

            for childnode in next_nodes:
                key = tuple(childnode.board.array) + (childnode.board.whitemove, childnode.board.whitecastle, childnode.board.blackcastle,childnode.board.enpassant_square)
                if key in self.hash_map:
                    new_value, new_line = self.hash_map[key]
                else:
                    new_value, new_line = self.abSearch(childnode, depth - 1, alpha, beta, False)
                    self.hash_map[key] = (new_value, new_line)
                value = max(value, new_value)
                if value >= beta:
                    break
                if value > alpha:
                    alpha = value
                    line = [childnode]
                    line.extend(new_line)
            return value, line

        else:
            value = 99999
            next_nodes = node.next_nodes
            #Sort in ascending order, we want to check the highest scoring nodes for minimizing player
            next_nodes.sort(key = self.nodeSort)
            line = []

            # If we are in the first layer, multithreading will be true, spawn processes
            if self.multithreading:

                # No need to check if nodes are already in hash map, we are on the first layer
                inputs = []
                for node in next_nodes:
                    inputs.append([node] + [depth - 1, alpha, beta, True])
                pool = multiprocessing.Pool(processes=NUM_PROCESSES)
                # make a new object, pass the last hash map, set it to be single-threaded
                ab = AlphaBeta(self.last_hash_map, False)
                results = pool.map(ab.abSearchMulti, inputs)

                # TODO: find best node, add all nodes to hash map
                sorted_results = sorted(zip(inputs, results), key=lambda x: x[1][0], reverse=False)

                for result in sorted_results:
                    childnode = result[0][0]
                    key = tuple(childnode.board.array) + (
                    childnode.board.whitemove, childnode.board.whitecastle, childnode.board.blackcastle,
                    childnode.board.enpassant_square)
                    if not (key in self.hash_map):
                        self.hash_map[key] = (result[1][0], result[1][0])

                line = [sorted_results[0][0][0]]
                line.extend(sorted_results[0][1][1])

                return sorted_results[0][1][0], line

            for childnode in next_nodes:
                key = tuple(childnode.board.array) + (childnode.board.whitemove, childnode.board.whitecastle, childnode.board.blackcastle, childnode.board.enpassant_square)
                if key in self.hash_map:
                    new_value, new_line = self.hash_map[key]
                else:
                    new_value, new_line = self.abSearch(childnode, depth - 1, alpha, beta, True)
                    self.hash_map[key] = (new_value, new_line)
                value = min(value, new_value)
                if value <= alpha:
                    break
                if value < beta:
                    beta = value
                    line = [childnode]
                    line.extend(new_line)
            return value, line


def getBestMoveSingle(node, depth, whiteplayer):
    last_hash_map = None

    for d in range(3,6):
        print("Searching depth: " + str(d))
        ab = AlphaBeta(last_hash_map, False)
        score, line = ab.abSearch(node, d, -99999, 99999, whiteplayer)
        last_hash_map = ab.hash_map

    return line[0], line

#TODO: pass depth to this function and save it as a global or class variable
#TODO: handle secondary search parameters here as well
def getBestMoveMulti(node, whiteplayer):
    last_hash_map = None

    for d in range(3,7):
        print("Searching depth: " + str(d))
        ab = AlphaBeta(last_hash_map, True)
        score, line = ab.abSearch(node, d, -99999, 99999, whiteplayer)
        last_hash_map = ab.hash_map

    return line[0], line



