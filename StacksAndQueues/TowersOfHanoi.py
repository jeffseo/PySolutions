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

    def isEmpty(self):
        return len(self.stackList) == 0

    def __len__(self):
        return len(self.stackList)

    def __str__(self):
        return str(self.stackList)

class TowerOfHanoi(object):
    def __init__(self):
        self.pegList = [Stack(), Stack(), Stack()]
        self.numOfDisks = 0

    def add(self,disk):
        if not self.pegList[0].isEmpty() and self.pegList[0].peek() <= disk:
            print "Error placing disk" + str(disk)
        else:
            self.pegList[0].push(disk)
            self.numOfDisks += 1

"""
To move disks from peg A to C
1. move (n-1) disk from peg A to B using C and intermediate Peg
2. move Nth disk from peg A to C
3. move (n-1) disk from B to C using A as intermediate peg
T(N) = T(N-1) + 1 + T(N-1) = 2T(N-1) + 1 // recurrence relation
T(N) = (2^N) - 1 
T(N) = # of steps required to move disks from src to dst

hanoi(N, source, destination, auxilary)
"""

    def move(self, n, src, dest, aux):
        if n > 1:
            self.move(n - 1, src, aux, dest)
            self.move(1, src, dest, aux)
            self.move(n-1, aux, dest, src)
        else:
            self.pegList[dest].push(self.pegList[src].pop())
            print src, "->", dest

    # call move to start the computation of recursive solution
    def hanoi(self, h):
        for i in range(h,0,-1): #goes backwards 3,2,1
            self.add(i)
        print '0:',self.pegList[0]
        print '1:',self.pegList[1]
        print '2:',self.pegList[2]
        self.move(h, 0, 2, 1) #0, 1, 2 refers to each stack in the pegList
        print '0:',self.pegList[0]
        print '1:',self.pegList[1]
        print '2:',self.pegList[2]

if __name__ == '__main__':
    test = TowerOfHanoi()
    test.hanoi(3)
