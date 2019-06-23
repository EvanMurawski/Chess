from BoardRep import BoardRep

class AlphaBeta:


    @staticmethod
    def alphabetaMove(rootNode, targetdepth, currentdepth=0):

        best_node = None
        b = 99999
        best_score = -9999

        if rootNode.next_nodes is None:
            rootNode.buildNextLayer()

        if rootNode.board.whitemove:

            for node in rootNode.next_nodes:
                if node.move_squares == [37, 28]:
                    print("found")

                node.minimax = AlphaBeta.minValue(node, targetdepth, currentdepth+1, best_score, b)
                #print("move; " + BoardRep.numbersToAlg(node.move_squares))
                #print("score: " + str(node.minimax) + "\n\n")
                if best_node is None or node.minimax > best_node.minimax:
                    best_node = node
                    best_score = node.minimax
        else:
            for node in rootNode.next_nodes:
                node.minimax = AlphaBeta.maxValue(node, targetdepth, currentdepth+1, best_score, b)
                #print("move; " + BoardRep.numbersToAlg(node.move_squares))
                #print("score: " + str(node.minimax) + "\n\n")
                if best_node is None or node.minimax < best_node.minimax:
                    best_node = node
                    best_score = node.minimax

        return best_node




    @staticmethod
    def maxValue(node, targetdepth, currentdepth, alpha, beta):
        if targetdepth == currentdepth:
            return node.score

        value = -99999

        idx = 0
        if node.next_nodes is None:
            node.buildNextLayer()

        for next_node in node.next_nodes:
            next_node_value = AlphaBeta.minValue(next_node, targetdepth, currentdepth+1, alpha, beta)
            if next_node_value > beta:
                best_node_idx = idx
                value = next_node_value
            idx += 1
            alpha = max(alpha, value)

        #node.best_node_idx = best_node_idx
        return value

    @staticmethod
    def minValue(node, targetdepth, currentdepth, alpha, beta):
        if targetdepth == currentdepth:
            return node.score
        value = 99999

        idx = 0
        found = False
        if node.next_nodes is None:
            node.buildNextLayer()

        for next_node in node.next_nodes:
            next_node_value = AlphaBeta.maxValue(next_node, targetdepth, currentdepth+1, alpha, beta)
            if next_node_value < alpha:
                best_node_idx = idx
                value = next_node_value
            idx += 1
            beta = min(beta, value)
        #node.best_node_idx = best_node_idx

        return value

