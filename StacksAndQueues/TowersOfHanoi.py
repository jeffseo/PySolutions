"""
In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different
sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending
order of size from top to bottom (e.g., each disk sits on top of an even larger one). You
have the following constraints:
(A) Only one disk can be moved at a time.
(B) A disk is slid off the top of one rod onto the next rod.
(C) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first rod to the last using Stacks.
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

class Tower(object):
    def __init__(self):
        self.rodList = [Stack(), Stack(), Stack()]
        