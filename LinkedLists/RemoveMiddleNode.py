"""
2.3
Implement an algorithm to delete a node in the middle of a single linked list, given
only access to that node.
EXAMPLE
Input: the node 'c' from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e
"""
from LinkedList import Node
import random

"""
Copy the data from the next node into this node and delete
the next node... wow
"""
def remove_middle_node(middle_node):
    if middle_node and middle_node.next:
        next_node = middle_node.next
        middle_node.data = next_node.data
        middle_node.next = next_node.next

if __name__ == '__main__':
    header = Node(random.randint(0,10))

    itr_node = header
    for i in range(9):
        itr_node.next = Node(random.randint(0,10))
        itr_node = itr_node.next

    print 'Pre-remove'
    itr_node = header
    while itr_node:
        print itr_node.data
        itr_node = itr_node.next

    print 'Post-remove'
    itr_node = header
    for i in range(9):
        if i == 4: #middle
            remove_middle_node(itr_node)
        else:
            itr_node = itr_node.next

    itr_node = header
    while itr_node:
        print itr_node.data
        itr_node = itr_node.next

