class Tree():

    @staticmethod
    def buildTree(rootNode, depth, current_depth=0):
        if current_depth == depth:
            return

        next_moves = rootNode.board.getLegalMoves()
        rootNode.setNextNodes(next_moves)

        for node in rootNode.next_nodes:
            Tree.buildTree(node, depth, current_depth+1)