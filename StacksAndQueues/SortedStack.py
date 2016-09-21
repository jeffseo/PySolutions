"""
3.6
Write a program to sort a stack in ascending order. You should not make any assumptions
about how the stack is implemented. The following are the only functions that
should be used to write this program: push | pop | peek | isEmpty.
"""

# Idea is to use two stacks. pop s1 and push to s2. if incoming value violates the sort order,
# pop from s2 and push to s1 until incoming value does not violate sort order.

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

def SortStack(stack):
    orderedStack = Stack()
    while not stack.isEmpty():
        newValue = stack.pop()
        while not orderedStack.isEmpty() and orderedStack.peek() > newValue:
            stack.push(orderedStack.pop())
        orderedStack.push(newValue)
    return orderedStack

if __name__ == '__main__':
    test = Stack()
    test.push(3)
    test.push(2)
    test.push(1)
    t2 = SortStack(test)

    assert t2.pop() == 3
    assert t2.pop() == 2
    assert t2.pop() == 1
        
