"""
http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
Check if a tree is a BST

A binary search tree (BST) is a node based binary tree data structure which has the following properties.
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""
import sys

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


# Note it's not enough checking if only left and right nodes are smaller than root as it does not ensure
# the subtrees within the tree follow the BST properties.

# One way to ensure a tree is BST:
# 1. Ensure the Max value from the left subtree is less than the current value
# 2. Ensure the Min value from the right subtree is greater than the current value
# This method requires two additional methods, getMin and getMax
def getMin(root):
    if root is None:
        return sys.maxint

    return min(root.data, min(getMin(root.left), getMin(root.right)));

def getMax(root):
    if root is None:
        return -sys.maxint - 1

    return max(root.data, max(getMax(root.left), getMax(root.right)))

def checkIfBST_1(root):
    pass


if __name__ == '__main__':
    t1 = Node(1)
    t1.left = Node(0)
    t1.right = Node(2)

    print getMax(t1)





