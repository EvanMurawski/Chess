from BoardRep import BoardRep
import multiprocessing



#todo, try alpha beta search from root node e.g. dont' seperately evaluate all legal moves
#todo, store the score in the node, start searching highest scoring nodes first
def alphabeta(node, depth, alpha, beta, maximizingplayer):



    if depth == 0:
        return node.score


    if node.next_nodes is None:
        node.buildNextLayer()


    if maximizingplayer:
        value = -99999

        for childnode in node.next_nodes:
            value = max(value, alphabeta(childnode, depth-1, alpha, beta, False))
            if value >= beta:
                break
            alpha = max(alpha, value)

        return value

    else:
        value = 99999
        for childnode in node.next_nodes:
            value = min(value, alphabeta(childnode, depth-1, alpha, beta, True))
            if value <= alpha:
                break
            beta = min(beta, value)
        return value


def getBestMoveWhite(node, depth):

    if node.next_nodes is None:
        node.buildNextLayer()

    bestscore = -999999999
    bestnode = None

    for childnode in node.next_nodes:
        value = alphabeta(childnode, depth, -99999, 99999, False)
        if value > bestscore:
            bestnode = childnode
            bestscore = value

        childnode.board.print()
        print("above value: ", str(value))

    return bestnode

def funcformulti(node):
    return alphabeta(node, 3, -99999, 99999, False)

def getBestMoveMulti(node, depth):
    pool = multiprocessing.Pool(processes=8)

    if node.next_nodes is None:
        node.buildNextLayer()

    bestscore = -999999999
    bestnode = None

    inputs = node.next_nodes
    outputs = pool.map(funcformulti, inputs)

    for (childnode, childscore) in zip(node.next_nodes, outputs):
        #childnode.board.print()
        #print("above value: ", str(childscore))

        if childscore > bestscore:
            bestnode = childnode
            bestscore = childscore

    return bestnode


