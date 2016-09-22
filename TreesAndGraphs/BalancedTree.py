""" 4.1
Implement a function to check if a tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
from the root by more than one.
"""

"""
Brute-force: Iteratively go through each node of tree and count number of steps of each leaf nodes.
Thinking about it, really only need to check the difference between the longest leaf node and shortest.
"""

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def IsLeaf(self):
        return self.leftChild == None and self.rightChild == None

    def insert(self,node):
        if node.data > self.data:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        elif node.data <= self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        
def maxDepth(self, root):
    if (root == None):
        return 0
    return 1 + max(maxDepth(root.leftChild), maxDepth(root.rightChild))

def minDepth(self, root):
    if (root == None):
        return 0
    return 1 + min(minDepth(root.leftChild), minDepth(root.rightChild))

def isBalanced(self):
    return (self.maxDepth() - self.minDepth() <= 1)

if __name__ == '__main__':
