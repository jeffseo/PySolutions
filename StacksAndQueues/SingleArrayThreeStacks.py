"""
3.1
Describe how you could use a single array to implement three stacks

Stacks = LIFO (Last in, First Out)
Operations include: push, pop, peek, isEmpty
Requires: a pointer to track the top

1: split the array into 3
[0,n/3) [n/3,2n/3) [2n/3,n)

"""

class ThreeStack(object):

    def __init__(self, stackSize = 100):
        self.arrayList = [None] * stackSize * 3
        self.stackPointer = [0,0,0] # stack pointers to track top elem

    def push(self, stackNum, value):
        # find index of the top element in the array + 1, and increment the stack pointer
        index = stackNum * stackSize + stackPointer[stackNum] + 1
        stackPointer[stackNum] += 1
        arrayList[index] = value

    def pop(self, stackNum):
        index = stackNum * stackSize + stackPointer[stackNum]
        retVal = arrayList[index]
        arrayList[index] = None
        stackPointer[stackNum] -= 1
        return retVal

    def peek(self, stackNum):
        index = stackNum * stackSize + stackPointer[stackNum]
        return arrayList[index]

    def isEmpty(self, stackNum):
        return stackPointer[stackNum] == stackNum*stackSize
