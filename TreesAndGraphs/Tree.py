class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
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
    #another exmaple: http://www.geeksforgeeks.org/find-the-minimum-element-in-a-binary-search-tree/
    def min(self):
        if self:
            if self.left is None:
                return self.data
            else:
                return self.left.min()
                
    """
    To delete a node in a tree, there are 3 scenarios to consider:
    1. Leaf node
    2. node with single child
    3. node with double child
    """

    def delete(self, value, parentNode):
        if value > self.data:
            if self.right:
                self.right.delete(value,self)
        elif value < self.data:
            if self.left:
                self.left.delete(value,self)
        else:
            if self.isLeafNode(): # node with no child
                if parentNode.left is self:
                    parentNode.left = None
                else:
                    parentNode.right = None
            elif self.left is not None and self.right is not None: #node with two child
                self.data = self.right.min()
                self.right.delete(self.data,self)
            elif self.left is not None: #node with single child
                if parentNode.left is self:
                    parentNode.left = self.left
                else:
                    parentNode.right = self.left
            else:
                if parentNode.left is self:
                    parentNode.left = self.right
                else:
                    parentNode.right = self.right

    def isLeafNode(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

class Tree:
    def __init__(self, treeNode=None):
        if isinstance(treeNode, int):
            self.root = TreeNode(treeNode)
        else:
            self.root = treeNode

    def __str__(self):
        if self.root:
            return str(self.root.data)
        else:
            return ""

    def insert(self, node):
        if node:
            if isinstance(node,int):
                self.root.insert(TreeNode(node))
            else:
                self.root.insert(node)

    def delete(self, value):
        if self.root:
            if self.root.data == value:
                tempRoot = TreeNode(0)
                tempRoot.left = self.root
                self.root.delete(value,tempRoot)
                self.root = tempRoot.left
            else:
                self.root.delete(value, None)

    def print_tree_in_order(self):
        print "Printing Tree In-order"
        self._print_in_order(self.root)

    def print_tree_pre_order(self):
        print "Printing Tree pre-order"
        self._print_pre_order(self.root)

    def print_tree_post_order(self):
        print "Printing Tree post-order"
        self._print_post_order(self.root)

    def _print_in_order(self, node):
        if node:
            self._print_in_order(node.left)
            print node.data
            self._print_in_order(node.right)

    def _print_pre_order(self, node):
        if node:
            print node.data
            self._print_pre_order(node.left)
            self._print_pre_order(node.right)

    def _print_post_order(self, node):
        if node:
            self._print_post_order(node.left)
            self._print_post_order(node.right)
            print node

if __name__ == '__main__':
    tree = Tree(1)
    tree.insert(TreeNode(10))
    tree.insert(TreeNode(15))
    tree.insert(TreeNode(4))
    tree.print_tree_pre_order()
    tree.insert(5)
    tree.delete(4)
    tree.print_tree_pre_order()
    tree.delete(1)
    tree.print_tree_pre_order()
