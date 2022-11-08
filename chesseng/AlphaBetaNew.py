import multiprocessing
from chesseng.BoardRep import BoardRep

def nodeSort(node):
    if BoardRep.isInCheck(node.board):
        return 0

    if node.board.is_capture:
        return 5

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
    return alphabeta(node, 3, -99999, 99999, False)

def multiAlphaBetaWhite(node):
    return alphabeta(node, 3, -99999, 99999, True)

def getBestMoveMulti(node, whiteplayer):
    pool = multiprocessing.Pool(processes=8)

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
    else:
        outputs = pool.map(multiAlphaBetaWhite, inputs)

    for (childnode, childscore) in zip(node.next_nodes, outputs):

        #childnode.board.print()
        #print("above value: ", str(childscore))

        if whiteplayer:
            if childscore > bestscore:
                bestnode = childnode
                bestscore = childscore
        else:
            if childscore < bestscore:
                bestnode = childnode
                bestscore = childscore

    return bestnode


