from core.node import node

def back_propagation(node: node, scores: list):
    while node is not None:
        for i in range(len(scores)):
            node.scores[i] += scores[i]
        node.visits += 1
        node = node.parent