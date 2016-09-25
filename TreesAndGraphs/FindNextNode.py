"""
4.5
Write an algorithm to find the 'next' node (e.g., in-order successor) of a given node in
a binary search tree where each node has a link to its parent.
"""

"""
in-order: left current right
# Refer to pg127 in CtCI for recursive implementation
"""

class Node(object):
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.parent = None

    def setParent(self, parentNode):
        self.parent = parentNode

    def setLeft(self, leftNode):
        self.left = leftNode
        leftNode.parent = self

    def setRight(self, rightNode):
        self.right = rightNode
        rightNode.parent = self

def FindNext(node):
    if node is None:
        return

    current = node
    while True:
        if current.parent == None:
            break
        current = current.parent

    # We now have the parent node. Traverse in-order until we hit the 'node'
    # and return the next node
    stack = []
    found = False
    done = False
    while not done:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) != 0:
                current = stack.pop()
                if found == True:
                    return current
                if current is node and found == False:
                    found = True
                current = current.right
            else:
                done =True
    return None

if __name__ == '__main__':
    root = Node(0)

    root.setLeft(Node(1))
    root.setRight(Node(2))
    root.left.setLeft(Node(3))
    root.right.setRight(Node(4))
    test = FindNext(root.left.left)
    print test.data
    assert test is root.left


