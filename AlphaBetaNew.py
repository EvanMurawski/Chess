from BoardRep import BoardRep

class AlphaBetaNew:


    def alphabeta(node, depth, alpha, beta, maximizingplayer):

        if node.next_nodes is None:
            node.buildNextLayer()

        if depth == 0:
            return node.score

        if maximizingplayer:
            value = -99999

            for childnode in node.next_nodes:
                value = max(value, AlphaBetaNew.alphabeta(childnode, depth-1, alpha, beta, False))
                if value >= beta:
                    break
                alpha = max(alpha, value)

            return value

        else:
            value = 99999
            for childnode in node.next_nodes:
                value = min(value, AlphaBetaNew.alphabeta(childnode, depth-1, alpha, beta, True))
                if value <= alpha:
                    break
                beta = min(beta, value)
            return value

    @staticmethod
    def getBestMoveWhite(node, depth):

        if node.next_nodes is None:
            node.buildNextLayer()

        bestscore = -999999999
        bestnode = None

        for childnode in node.next_nodes:
            value = AlphaBetaNew.alphabeta(node, 5, -99999, 99999, True)
            if value > bestscore:
                bestnode = childnode

        return bestnode





