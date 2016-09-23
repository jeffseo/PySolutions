"""
Implement BFS and DFS traversal of trees

DFS uses a stack
BFS uses a queue
"""

class Queue(object):
    def __init__(self):
        self.list = []

    def enqueue(self, node):
        self.list.insert(0, node)

    def dequeue(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

class Stack(object):
    def __init__(self):
        self.list = []

    def push(self, node):
        self.list.append(node)

    def pop(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

    def peek(self):
        return self.list[-1]

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
searches a node and its siblings before going on to any children
Uses a queue to remember to get the next vertex to start a search when a dead end occurs in any iteration
Employs the following rules:
Visit adjacent unvisited vertex. Mark it as visited. Display it. Insert it in a queue.
If no adjacent vertex is found, remove first vertex from queue (basically dequeue).
Repeat rule 1 and rule 2 until queue is empty

"""
def BreadthFirstSearch(root, searchValue):
    print 'BFS:'
    tracker = Queue()
    tracker.enqueue(root)

    while tracker.size() != 0:
        node = tracker.dequeue()
        if node.data == searchValue:
            return True
        else:
            if node.left != None:
                tracker.enqueue(node.left)
            if node.right != None:
                tracker.enqueue(node.right)
            print node.data
    return False

def PostOrderTraversal(root):
    if root == None:
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print root.data

# NOTE: DFS on a tree is equivalent to post-order traversal
def DepthFirstSearch(root):
    print 'DFS:'
    PostOrderTraversal(root)

    # tracker = Stack()
    # tracker.push(root)

    # while tracker.size() != 0:
    #     node = tracker.pop()
    #     if node.right != None and node.right not in visited:
    #         tracker.push(root.right)
    #         visited.append(node.right)
    #     if node.left != None and node.left not in visited:
    #         tracker.push(root.left)
    #         visited.append(node.left)
    #     print node.data

if __name__ == "__main__":
    print "\n\
           1        \n\
          / \\      \n\
         2   3      \n\
        / \\        \n\
       4  5"
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    BreadthFirstSearch(root, 6)
    DepthFirstSearch(root)



