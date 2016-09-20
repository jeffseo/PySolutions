"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
in real life, we would likely start a new stack when the previous stack exceeds
some threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
Stacks should be composed of several stacks, and should create a new stack once
the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
behave identically to a single stack (that is, pop() should return the same values as it
would if there were just a single stack).

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific
sub-stack.
- Need to implement a rollover system i.e. pop an element from stack 1, need to remove
the bottom of stack 2 and push it onto stack 1, and so forth...
-- Rather than doing this, it may be OK with some stacks not being at full capacity...
This would improve the time complexity, but it might get us into tricky situations later
on if someone assumes that all stacks (other than the last) operate at full capacity...

THIS IS THE TRADE OFF!!!
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

    def __len__(self):
        return len(self.stackList)

    def __str__(self):
        return str(self.stackList)

class SetOfStacks(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.stackTracker = [Stack()]

    def push(self, data):
        if len(self.stackTracker[-1]) >= self.capacity:
            newStack = Stack()
            newStack.push(data)
            self.stackTracker.append(newStack)
        else:
            self.stackTracker[-1].push(data)

    def pop(self):
        retVal = self.stackTracker[-1].pop()
        if len(self.stackTracker[-1]) == 0:
            self.stackTracker.pop()
        return retVal

    def popAt(self, stackNum):
        retVal = self.stackTracker[stackNum].pop()
        if len(self.stackTracker[stackNum]) == 0:
            self.stackTracker.pop()
        return retVal

    def __str__(self):
        retStr = ''
        for idx, stack in enumerate(self.stackTracker):
            retStr += 'stack #' + str(idx) + ':' + str(stack) + '\n'
        return retStr

if __name__ == "__main__":
    A = SetOfStacks(10)
    for i in range(10):
        A.push(i)
    print A
    A.push(1)
    print A
    A.pop()
    print A
    A.push(1)
    print A
    A.popAt(1)
    print A

