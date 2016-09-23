"""
4.4
Given a binary search tree, design an algorithm which creates a linked list of all the
nodes at each depth (eg, if you have a tree with depth D, you'll have D linked lists).
Since we want all nodes at each depth, want to use BFS method.
BFS uses a queue to track nodes.

"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createLinkedList(root):
    if root is None:
        return []

    result = []
    queue = [root]
    temp = UnorderedList()
    num_of_nodes_in_current_depth = 1

    while True:
        if num_of_nodes_in_current_depth == 0:
            num_of_nodes_in_current_depth = len(queue)
            result.append(temp)
            temp = UnorderedList()

        if len(queue) == 0:
            break

        current = queue.pop()
        temp.add(current.value)

        if current.left != None:
            queue.insert(0,current.left)
        if current.right != None:
            queue.insert(0,current.right)
        num_of_nodes_in_current_depth -= 1
    return result

if __name__ == '__main__':
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

    testList = createLinkedList(root)
    for i,linkedList in enumerate(testList):
        print 'depth',i,':'
        current = linkedList.head
        while current != None:
            print current.getData()
            current = current.getNext()
