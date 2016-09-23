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

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

# Iterative function for inorder tree traversal
def inOrder(root):
     
    # Set current to root of binary tree
    current = root 
    s = [] # initialze stack
    done = 0
     
    while(not done):
         
        # Reach the left most Node of the current Node
        if current is not None:
             
            # Place pointer to a tree node on the stack 
            # before traversing the node's left subtree
            s.append(current)
         
            current = current.left 
         
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is 
        # empty you are done
        else:
            if(len(s) >0 ):
                current = s.pop()
                print current.data,
         
                # We have visited the node and its left 
                # subtree. Now, it's right subtree's turn
                current = current.right 
 
            else:
                done = 1

# An iterative process to print preorder traveral of BT
# pre-order (root, left, right)
def iterativePreorder(root):
     
    # Base CAse 
    if root is None:
        return
 
    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)
 
    #  Pop all items one by one. Do following for every popped item
    #   a) print it
    #   b) push its right child
    #   c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while(len(nodeStack) > 0):
         
        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print node.data,
         
        # Push right and left children of the popped node
        # to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

# An iterative function to do postorder traversal of a
# given binary tree using 2 stacks
def postOrderIterative2(root): 
    if root is None:
        return         
     
    # Create two stacks 
    s1 = []
    s2 = []
     
    # Push root to first stack
    s1.append(root)
     
    # Run while first stack is not empty
    while (len(s1) >0):
         
        # Pop an item from s1 and append it to s2
        node = s1.pop()
        s2.append(node)
     
        # Push left and right children of removed item to s1
        if node.left is not None:
            s1.append(node.left)
        if node.right is not None :
            s1.append(node.right)
 
        # Print all eleements of second stack
    while(len(s2) > 0):
        node = s2.pop()
        print node.data,

def postOrderIterative(root):
    if root is None:
        return
    ans = []
    stack = []

    while True:
        while root:
            # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            # Set root as root's left child
            root = root.left

        # Pop an item from stack and set it as root
        root = stack.pop()
 
        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and peek(stack) == root.right):
            stack.pop() # Remove right child from stack 
            stack.append(root) # Push root back to stack
            root = root.right # change root so that the 
                             # righ childis processed next
 
        # Else print root's data and set root as None
        else:
            ans.append(root.data) 
            root = None
 
        if (len(stack) <= 0):
            return ans

def PostOrderTraversal(root):
    if root == None:
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print root.data

#WIP: This is not DFS
# NOTE: DFS on a tree is equivalent to post-order traversal
def DepthFirstSearch(root):
    print 'DFS:'
    #return PostOrderTraversal(root)

    visited = []
    tracker = Stack()
    tracker.push(root)

    while tracker.size() != 0:
        node = tracker.pop()
        visited.append(node)
        if node.right != None:
            tracker.push(node.right)
        if node.left != None:
            tracker.push(node.left)
    return visited

#http://www.geeksforgeeks.org/iterative-preorder-traversal/
if __name__ == "__main__":
    print "\n\
           1        \n\
          / \\      \n\
         2   3      \n\
        / \\        \n\
       4   5"
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    BreadthFirstSearch(root, 6)

    result = []
    for i in DepthFirstSearch(root):
        result.append(i.data)
    print result

    print "Post Order traversal of binary tree is"
    print postOrderIterative(root)




