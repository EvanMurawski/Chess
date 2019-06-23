from BoardRep import BoardRep

class MiniMax:


    @staticmethod
    def minimaxMove(rootNode, targetdepth, currentdepth=0):

        best_node = None
        if rootNode.next_nodes is None:
            rootNode.buildNextLayer()

        if rootNode.board.whitemove:

            for node in rootNode.next_nodes:
                if node.move_squares == [37, 28]:
                    print("found")

                node.minimax = MiniMax.minValue(node, targetdepth, currentdepth+1)
                #print("move; " + BoardRep.numbersToAlg(node.move_squares))
                #print("score: " + str(node.minimax) + "\n\n")

            for node in rootNode.next_nodes:
                if best_node is None or node.minimax > best_node.minimax:
                    best_node = node
        else:
            for node in rootNode.next_nodes:
                node.minimax = MiniMax.maxValue(node, targetdepth, currentdepth+1)
                #print("move; " + BoardRep.numbersToAlg(node.move_squares))
                #print("score: " + str(node.minimax) + "\n\n")

            for node in rootNode.next_nodes:
                if best_node is None or node.minimax < best_node.minimax:
                    best_node = node

        return best_node




    @staticmethod
    def maxValue(node, targetdepth, currentdepth):
        if targetdepth == currentdepth:
            return node.score

        value = -99999

        idx = 0
        if node.next_nodes is None:
            node.buildNextLayer()

        for next_node in node.next_nodes:
            next_node_value = MiniMax.minValue(next_node, targetdepth, currentdepth+1)
            if next_node_value > value:
                best_node_idx = idx
                value = next_node_value
            idx += 1

        #node.best_node_idx = best_node_idx
        return value

    @staticmethod
    def minValue(node, targetdepth, currentdepth):
        if targetdepth == currentdepth:
            return node.score
        value = 99999

        idx = 0
        found = False
        if node.next_nodes is None:
            node.buildNextLayer()

        for next_node in node.next_nodes:
            next_node_value = MiniMax.maxValue(next_node, targetdepth, currentdepth+1)
            if next_node_value < value:
                best_node_idx = idx
                value = next_node_value
                found = True
        if not found:
            print("notfound")
        #node.best_node_idx = best_node_idx

        return value

