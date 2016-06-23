class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self, treeNode=None):
        self.root = treeNode

    def __str__(self):
        if self.root:
            return str(self.root.data)
        else:
            return ""

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

    def print_tree_in_order(self):
        print "Printing Tree In-order"
        self._print_in_order(self.root)

    def print_tree_pre_order(self):
        print "Printing Tree pre-order"
        self._print_pre_order(self.root)

    def print_tree_post_order(self):
        print "Printing Tree post-order"
        self._print_post_order(self.root)

if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    tree = Tree(test)
    tree.print_tree_in_order()
    tree.print_tree_post_order()
    tree.print_tree_pre_order()