""" 3.5
Implement a MyQueue class which implements a queue using two stacks.
"""

class Stack(object):
    def __init__(self):
        self.stackList = []

    def push(self, data):
        self.stackList.append(data)

    def pop(self):
        return self.stackList.pop()

    def peek(self):
        return self.stackList[-1]

    def isEmpty(self):
        return len(self.stackList) == 0

    def __len__(self):
        return len(self.stackList)

    def __str__(self):
        return str(self.stackList)

# FIFO: First-in First-out
# Method 1. Use the second stack to reverse the order of elements (pop s1 and push to s2)
# on each peek/pop, pop everything from s1 onto s2 and perform a peek/pop operation, and push
# everything back.
# 
# Method 2. Let elements sit in s2
# s1 will be ordered with the newest elements on top, while s2 will have the oldest elements
# on top. we push the new elements onto s1, and peek and pop from s2. when s2 is empty, we'll
# transfer all elements from s1 onto s2, in reverse order
class MyQueue(object):
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()

    def enqueue(self, data):
        self.stack_one.push(data)

    def dequeue(self):
        if self.stack_two.isEmpty():
            while not self.stack_one.isEmpty():
                self.stack_two.push(self.stack_one.pop())
        return self.stack_two.pop()

    def peek(self):
        if self.stack_two.isEmpty():
            while not self.stack_one.isEmpty():
                self.stack_two.push(self.stack_one.pop())
        return self.stack_two.peek()

if __name__ == '__main__':
    test = MyQueue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)

    assert test.dequeue() == 1

