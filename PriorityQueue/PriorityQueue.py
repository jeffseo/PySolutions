#Priority Queue implementation
from abc import ABCMeta, abstractmethod

class PriorityQueue(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, obj):
        raise NotImplementedError()

    @abstractmethod
    def remove(self):
        raise NotImplementedError()

    @abstractmethod
    def size(self):
        pass

class PriorityObject(object):
    def __init__(self, priority=0, value=0):
        self.priority = priority
        self.value = value
        self.nextNode = None
        self.leftChild = None
        self.rightChild = None

# Either sorted or unsorted
# Sorted: Insert - O(N), RemoveMax - O(1)
# Unsorted: Insert - O(1), RemoveMax - O(N)
class PriorityQueue_Array(PriorityQueue):

    def __init__(self):
        self.queue = []
        self.numberOfItems = 0

    def insert(self, obj):
        self.queue.append(obj)
        #sorted(self.queue, key=lambda temp: temp.priority)
        self.queue.sort(key=lambda temp: temp.priority)
        self.numberOfItems += 1

    def remove(self):
        if self.numberOfItems > 0:
            self.numberOfItems -= 1
            return self.queue.pop()
        else:
            raise 'Queue empty'

    def size(self):
        return self.numberOfItems

    def __str__(self):
        string = "["
        for i in self.queue:
            string += str(i.value) + ','
        string += ']'
        return string

# Same as Array:
# Sorted: Insert - O(N), Remove max - O(1)
# Unsorted: Insert - O(1), Remove max - O(N)
# For linked list, we sort the list in order from high to low, since removing the 
# front of the list can be done in O(1) time. (We could also use a tail pointer to
# negate the need for this)
class PriorityQueue_LinkedList(PriorityQueue):

    def __init__(self):
        self.head = None
        self.numberOfItems = 0

    def insert(self, obj):
        self.numberOfItems += 1
        if self.head == None:
            self.head = obj
        else:
            previous = self.head
            current = self.head.nextNode
            while current != None:
                if current.priority < obj.priority:
                    previous.nextNode = obj
                    obj.nextNode = current
                    return
                else:
                    previous = current
                    current = current.nextNode
            previous.nextNode = obj

    def remove(self):
        returnNode = self.head
        self.head = returnNode.nextNode
        self.numberOfItems -= 1
        return returnNode

    def size(self):
        return self.numberOfItems

    def __str__(self):
        returnString = "["
        current = self.head
        while current != None:
            returnString += str(current.value) + ','
            current = current.nextNode
        returnString += "]"
        return returnString

class PriorityQueue_BST(object):

    def __init__(self):
        self.root = None
        self.numberOfItems = 0

    def insert(self, obj):
        if self.root == None:
            self.root = obj
        else:
            pass

    def remove(self):
        pass

    def size(self):
        return self.numberOfItems

    def __str__(self):
        pass

# To improve performance, priority queues typically use a heap as their backbone, 
# giving O(log n) performance for inserts and removals, and O(n log n) to build initially
# Using built in heapq.py, for implementation of Binary Heap, refer to TreesAndGraphs/BinaryHeap
class PriorityQueue_Heap(object):
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def insert(self, obj):
        pass

    def remove(self):
        pass

    def size(self):
        return len(self.arrayList)

    def heapify(self):
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    A = PriorityQueue_Array()
    B = PriorityQueue_LinkedList()
    stringDictionary = {A: "Array implementation",
                        B: "LinkedList implementation"}
    priorityQueueTypeTest = [A, B]
    for pq in priorityQueueTypeTest:
        print stringDictionary[pq]
        pq.insert(PriorityObject(5,1))
        print pq
        pq.insert(PriorityObject(0,3))
        print pq
        pq.insert(PriorityObject(0,2))
        print pq
        pq.insert(PriorityObject(5,10))
        print pq
        pq.remove()
        print pq        
