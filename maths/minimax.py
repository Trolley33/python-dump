__author__ = 'Reece'
from sys import maxsize


# TREE BUILDER
class Node():
    """
    Defines how a node is built.
    """
    def __init__(self, depth, max_depth, player, a_value, value=0):
        self.depth = depth
        self.max_depth = max_depth
        self.player = player
        self.a_value = a_value
        self.value = value
        self.children = []
        self.build_children()

    def build_children(self):
        if self.depth < self.max_depth:
            for i in range(1, 3):
                v = self.a_value - i
                child_node = Node(self.depth+1, self.max_depth, -self.player, v, self.value_of(v))
                self.children.append(child_node)

    def value_of(self, val):
        if val == 0:
            return maxsize * self.player
        elif val < 0:
            return maxsize * -self.player
        return 0

    def print_tree(self):
        print("Branch: " + str(self.depth), str(self.a_value), str(self.value))
        for b in self.children:
            b.print_tree()


def choose(node, depth, max_d, player):
    if (depth == max_d) or (abs(node.value) == maxsize):
        return node.value

    best_value = maxsize * -player

    for x in range(len(node.children)):
        child = node.children[x]
        val = choose(child, depth+1, max_d, -player)
        if abs(maxsize * -player - val) < abs(maxsize * -player - best_value):
            best_value = val

    return best_value

max_depth = 6
print("Depth, a_value, value")
Node(0, max_depth, 1, 10).print_tree()
input()