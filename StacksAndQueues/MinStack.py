import random
"""
How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? 
Push, pop and min should all operate in O(1) time.

1. One method is to use a node with a member variable min to keep track of
minimum values in the stack until that node.
2. other is to keep 2 stacks and track min with the other stack (TODO)
"""

class Node(object):
    def __init__(self,data,nextNode=None):
        self.data = data
        self.next = nextNode

class NodeWithMin(Node):
    def __init__(self,data,nextNode=None,minimum=0):
        Node.__init__(self,data,nextNode)
        self.min = minimum

class minStack:
    def __init__(self):
        self.head = None

    def Pop(self):
        if self.head:
            self.head = self.head.next

    def Push(self,nodeWithMin):
        if self.head is None:
            self.head = nodeWithMin
            self.head.min = nodeWithMin.data
        else:
            nodeWithMin.next = self.head
            self.head = nodeWithMin
            if self.head.data > self.head.next.min:
                self.head.min = self.head.next.min
            else:
                self.head.min = self.head.data

    def GetMin(self):
        if self.head:
            return self.head.min

    def PrintDebug(self):
        itr = self.head
        print "head"
        while itr is not None:
            print itr.data
            itr = itr.next
        print "bottom"
            

if __name__ == '__main__':
    stack = minStack()
    for i in range(10):
        randomVal = random.randint(0,10)
        node = NodeWithMin(randomVal)
        stack.Push(node)
    stack.PrintDebug()

    print "The minimum is: ", stack.GetMin()


