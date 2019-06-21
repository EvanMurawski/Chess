from BoardRep import BoardRep

class MiniMax:


    @staticmethod
    def minimaxMove(rootNode):

        best_node = None

        if rootNode.board.whitemove:
            for node in rootNode.next_nodes:
                node.minimax = MiniMax.maxValue(node)
                print("move; " + BoardRep.numbersToAlg(node.move_squares))
                print("score: " + str(node.minimax) + "\n\n")

            for node in rootNode.next_nodes:
                if best_node is None or node.minimax > best_node.minimax:
                    best_node = node
        else:
            for node in rootNode.next_nodes:
                node.minimax = MiniMax.minValue(node)
                print("move; " + BoardRep.numbersToAlg(node.move_squares))
                print("score: " + str(node.minimax) + "\n\n")

            for node in rootNode.next_nodes:
                if best_node is None or node.minimax < best_node.minimax:
                    best_node = node

        return best_node




    @staticmethod
    def maxValue(node):
        if node.next_nodes is None:
            return node.score
        value = -99999

        for next_node in node.next_nodes:
            value = max(value, MiniMax.minValue(next_node))

        return value

    @staticmethod
    def minValue(node):
        if node.next_nodes is None:
            return node.score
        value = 99999

        for next_node in node.next_nodes:
            value = min(value, MiniMax.maxValue(next_node))

        return value

