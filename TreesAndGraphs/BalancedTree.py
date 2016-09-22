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
    def __init__(self, data=0):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def IsLeaf(self):
        return self.leftChild == None and self.rightChild == None
        
def maxDepth(root):
    if (root == None):
        return 0
    return 1 + max(maxDepth(root.leftChild), maxDepth(root.rightChild))

def minDepth(root):
    if (root == None):
        return 0
    return 1 + min(minDepth(root.leftChild), minDepth(root.rightChild))

def isBalanced(root):
    return (maxDepth(root) - minDepth(root) <= 1)

if __name__ == '__main__':
    root = TreeNode()
    current = root
    for i in range(10):
        current.leftChild = TreeNode()
        current = current.leftChild

    root.rightChild = TreeNode()
    print maxDepth(root)
    print minDepth(root)
    assert isBalanced(root) == False

    root2 = TreeNode()
    current = root2
    for i in range(1):
        current.leftChild = TreeNode()
        current = current.leftChild

    current = root2
    for i in range(2):
        current.rightChild = TreeNode()
        current = current.rightChild

    print maxDepth(root2)
    print minDepth(root2)

    assert isBalanced(root2) == True

