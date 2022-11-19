import multiprocessing

MULTI_DEPTH_INITIAL = 3
MULTI_DEPTH_SECONDARY = 4
SECONDARY_NODE_QTY = 3
NUM_PROCESSES = 16


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
#todo, store the score in the node, start searching highest scoring nodes first
def alphabeta(node, depth, alpha, beta, maximizingplayer):

    if depth == 0:
        return node.getScore()

    if node.next_nodes is None:
        node.buildNextLayer()

    if maximizingplayer:
        value = -99999
        next_nodes = node.next_nodes
        next_nodes.sort(key = nodeSort)
        for childnode in next_nodes:
            value = max(value, alphabeta(childnode, depth-1, alpha, beta, False))
            if value >= beta:
                break
            alpha = max(alpha, value)
        return value

    else:
        value = 99999
        next_nodes = node.next_nodes
        next_nodes.sort(key = nodeSort)
        for childnode in next_nodes:
            value = min(value, alphabeta(childnode, depth-1, alpha, beta, True))
            if value <= alpha:
                break
            beta = min(beta, value)
        return value


def getBestMoveSingle(node, depth, whiteplayer):
    if node.next_nodes is None:
        node.buildNextLayer()

    if whiteplayer:
        bestscore = -999999999
    else:
        bestscore = 999999999

    bestnode = None

    for childnode in node.next_nodes:
        childscore = alphabeta(childnode, depth, -99999, 99999, not whiteplayer)

        if whiteplayer:
            if childscore > bestscore:
                bestnode = childnode
                bestscore = childscore
        else:
            if childscore < bestscore:
                bestnode = childnode
                bestscore = childscore


        # childnode.board.print()
        # print("above value: ", str(childscore))

    return bestnode

def multiAlphaBetaBlack(node):
    return alphabeta(node, MULTI_DEPTH_INITIAL, -99999, 99999, False)

def multiAlphaBetaWhite(node):
    return alphabeta(node, MULTI_DEPTH_INITIAL, -99999, 99999, True)

def multiAlphaBetaBlackSecondary(node):
    return alphabeta(node, MULTI_DEPTH_SECONDARY, -99999, 99999, False)

def multiAlphaBetaWhiteSecondary(node):
    return alphabeta(node, MULTI_DEPTH_SECONDARY, -99999, 99999, True)

#TODO: pass depth to this function and save it as a global or class variable
def getBestMoveMulti(node, whiteplayer):
    pool = multiprocessing.Pool(processes=NUM_PROCESSES)

    if node.next_nodes is None:
        node.buildNextLayer()

    if whiteplayer:
        bestscore = -999999999
    else:
        bestscore = 999999999

    bestnode = None

    inputs = node.next_nodes

    if whiteplayer:
        outputs = pool.map(multiAlphaBetaBlack, inputs)
        sorted_outputs = sorted(zip(node.next_nodes, outputs), key=lambda x: x[1], reverse=True)
        secondary_search_nodes = [sorted_outputs[x][0] for x in range(SECONDARY_NODE_QTY)]
        outputs = pool.map(multiAlphaBetaBlackSecondary, secondary_search_nodes)
        bestnode = sorted(zip(secondary_search_nodes, outputs), key=lambda x: x[1], reverse=True)[0][0]
    else:
        outputs = pool.map(multiAlphaBetaWhite, inputs)
        sorted_outputs = sorted(zip(node.next_nodes, outputs), key=lambda x: x[1])
        secondary_search_nodes = [sorted_outputs[x][0] for x in range(SECONDARY_NODE_QTY)]
        outputs = pool.map(multiAlphaBetaWhiteSecondary, secondary_search_nodes)
        bestnode = sorted(zip(secondary_search_nodes, outputs), key=lambda x: x[1])[0][0]


    return bestnode


