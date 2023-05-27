import multiprocessing
import chesseng.Node as Node

DEPTH_INITIAL = 3
DEPTH_FINAL = 5
SECONDARY_NODE_QTY = 3
SECONDARY_SEARCH = True
NUM_PROCESSES = 16


class AlphaBeta:

    def __init__(self, last_hash_map=None):
        if last_hash_map is None:
            self.last_hash_map = {}
        else:
            self.last_hash_map = last_hash_map

        self.hash_map = {}

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

    #todo, try alpha beta search from root node e.g. dont' seperately evaluate all legal moves
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

    for d in range(5,6):
        print("Searching depth: " + str(d))
        ab = AlphaBeta(last_hash_map)
        score, line = ab.abSearch(node, d, -99999, 99999, whiteplayer)
        last_hash_map = ab.hash_map

    return line[0], line

def multiAlphaBetaBlack(node):
    ab = AlphaBeta()
    return ab.abSearch(node, DEPTH_INITIAL, -99999, 99999, False), ab.hash_map

def multiAlphaBetaWhite(node):
    ab = AlphaBeta()
    return ab.abSearch(node, DEPTH_INITIAL, -99999, 99999, True), ab.hash_map

def multiAlphaBetaBlackSecondary(node):
    ab = AlphaBeta()
    return ab.abSearch(node, DEPTH_FINAL, -99999, 99999, False), ab.hash_map

def multiAlphaBetaWhiteSecondary(node):
    ab = AlphaBeta()
    return ab.abSearch(node, DEPTH_FINAL, -99999, 99999, True), ab.hash_map

#TODO: pass depth to this function and save it as a global or class variable
#TODO: handle secondary search parameters here as well
def getBestMoveMulti(node, whiteplayer):

    pool = multiprocessing.Pool(processes=NUM_PROCESSES)

    if node.next_nodes is None:
        node.buildNextLayer()

    inputs = node.next_nodes

    # TODO simplify this, redundant code
    if whiteplayer:
        results = pool.map(multiAlphaBetaBlack, inputs)
        outputs = results[0]
        sorted_outputs = sorted(zip(inputs, outputs), key=lambda x: x[1][0], reverse=True)
        if SECONDARY_SEARCH:
            inputs = [sorted_outputs[x][0] for x in range(min(SECONDARY_NODE_QTY, len(sorted_outputs)))]
            outputs = pool.map(multiAlphaBetaBlackSecondary, inputs)
            sorted_outputs = sorted(zip(inputs, outputs), key=lambda x: x[1], reverse=True)

        bestmove = sorted_outputs[0][0]
        end_node = sorted_outputs[0][1][1]
    else:
        results = pool.map(multiAlphaBetaWhite, inputs)
        outputs = results[0]
        sorted_outputs = sorted(zip(node.next_nodes, outputs), key=lambda x: x[1])

        if SECONDARY_SEARCH:
            inputs = [sorted_outputs[x][0] for x in range(min(SECONDARY_NODE_QTY, len(sorted_outputs)))]
            outputs = pool.map(multiAlphaBetaWhiteSecondary, inputs)
            sorted_outputs = sorted(zip(inputs, outputs), key=lambda x: x[1])

        bestmove = sorted_outputs[0][0]
        end_node = sorted_outputs[0][1][1]


    return bestmove, end_node


