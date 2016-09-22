"""
4.3

Given a sorted (increasing order) array, write an algorithm to create a binary tree with
minimal height.

- Create a binary tree such that for each node, the number of nodes in the left subtree and the
right subtree are equal, if possible

1. Insert into the tree the middle element of the array
2. Insert (into the left subtree) the left subarray elements
3. Insert (into the right subtree) the right subarray elements
4. recurse
"""

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def addToTree(array, start, end):
    if end < start:
        return None

    middle = (end + start) // 2
    root = TreeNode(array[middle])
    root.left = addToTree(array, start, middle - 1)
    root.right = addToTree(array, middle + 1, end)
    return root

def createMinimalBST(array):
    return addToTree(array, 0, len(array) - 1)

def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print root.value
    printInOrder(root.right)

if __name__ == '__main__':
    t1 = [1,2,3,4,5,6,7,8,9]
    root = createMinimalBST(t1)
    printInOrder(root)
