import multiprocessing
import chesseng.Node as Node

MULTI_DEPTH_INITIAL = 3
MULTI_DEPTH_SECONDARY = 5
SECONDARY_NODE_QTY = 3
SECONDARY_SEARCH = False
NUM_PROCESSES = 16

#TODO improve this, e.g. prioritize captures of higher value pieces, maybe consider heuristic value of the node
def nodeSort(node):
    if node.board.isInCheck():
        return 0

    if node.board.is_capture:
        return 5

    # Black just moved, see if it is a forward move
    # From square is a lower row number -> is a forward move
    if node.board.whitemove and node.move_squares[0] // 8  < node.move_squares[1] // 8:
        return 8

    # White just moved, see if it is a forward move
    # From square is a higher row number -> is a forward move
    if (not node.board.whitemove) and node.move_squares[0] // 8 > node.move_squares[1] // 8:
        return 8


    return 10




#todo, try alpha beta search from root node e.g. dont' seperately evaluate all legal moves
#TODO, if there are no more nodes after building next layer (i.e. no more legal moves, return the score of the node
# (could be stalemate or checkmate)
def alphabeta(node, depth, alpha, beta, maximizingplayer):

    if depth == 0:
        return node.getScore(), []

    if node.next_nodes is None:
        node.buildNextLayer()

    if maximizingplayer:
        value = -99999
        next_nodes = node.next_nodes
        next_nodes.sort(key = nodeSort)
        line = []
        for childnode in next_nodes:
            new_value, new_line = alphabeta(childnode, depth-1, alpha, beta, False)
            value= max(value, new_value)
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
        next_nodes.sort(key = nodeSort)
        line = []
        for childnode in next_nodes:
            new_value, new_line = alphabeta(childnode, depth-1, alpha, beta, True)
            value = min(value, new_value)
            if value <= alpha:
                break
            if value < beta:
                beta = value
                line = [childnode]
                line.extend(new_line)
        return value, line


def getBestMoveSingle(node, depth, whiteplayer):
    if node.next_nodes is None:
        node.buildNextLayer()

    if whiteplayer:
        bestscore = -999999999
    else:
        bestscore = 999999999

    bestnode = None

    for childnode in node.next_nodes:
        childscore, line = alphabeta(childnode, depth, -99999, 99999, not whiteplayer)

        if whiteplayer:
            if childscore > bestscore:
                bestnode = childnode
                bestscore = childscore
                bestline =  line
        else:
            if childscore < bestscore:
                bestnode = childnode
                bestscore = childscore
                bestline = line


        # childnode.board.print()
        # print("above value: ", str(childscore))

    return bestnode, bestline

def multiAlphaBetaBlack(node):
    return alphabeta(node, MULTI_DEPTH_INITIAL, -99999, 99999, False)

def multiAlphaBetaWhite(node):
    return alphabeta(node, MULTI_DEPTH_INITIAL, -99999, 99999, True)

def multiAlphaBetaBlackSecondary(node):
    return alphabeta(node, MULTI_DEPTH_SECONDARY, -99999, 99999, False)

def multiAlphaBetaWhiteSecondary(node):
    return alphabeta(node, MULTI_DEPTH_SECONDARY, -99999, 99999, True)

#TODO: pass depth to this function and save it as a global or class variable
#TODO: handle secondary search parameters here as well
def getBestMoveMulti(node, whiteplayer):

    pool = multiprocessing.Pool(processes=NUM_PROCESSES)

    if node.next_nodes is None:
        node.buildNextLayer()

    inputs = node.next_nodes

    # TODO simplify this, redundant code
    if whiteplayer:
        outputs = pool.map(multiAlphaBetaBlack, inputs)
        sorted_outputs = sorted(zip(inputs, outputs), key=lambda x: x[1][0], reverse=True)
        if SECONDARY_SEARCH:
            inputs = [sorted_outputs[x][0] for x in range(min(SECONDARY_NODE_QTY, len(sorted_outputs)))]
            outputs = pool.map(multiAlphaBetaBlackSecondary, inputs)
            sorted_outputs = sorted(zip(inputs, outputs), key=lambda x: x[1], reverse=True)

        bestmove = sorted_outputs[0][0]
        end_node = sorted_outputs[0][1][1]
    else:
        outputs = pool.map(multiAlphaBetaWhite, inputs)
        sorted_outputs = sorted(zip(node.next_nodes, outputs), key=lambda x: x[1])

        if SECONDARY_SEARCH:
            inputs = [sorted_outputs[x][0] for x in range(min(SECONDARY_NODE_QTY, len(sorted_outputs)))]
            outputs = pool.map(multiAlphaBetaWhiteSecondary, inputs)
            sorted_outputs = sorted(zip(inputs, outputs), key=lambda x: x[1])

        bestmove = sorted_outputs[0][0]
        end_node = sorted_outputs[0][1][1]


    return bestmove, end_node


