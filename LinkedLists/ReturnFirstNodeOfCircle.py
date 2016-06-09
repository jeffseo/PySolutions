"""
2.5
Given a circular linked list, implement an algorithm which returns node at the beginning
of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an
earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
"""
from LinkedList import Node
import random

def get_head_of_circular_list(header_node):
    pointer_1 = header_node
    pointer_2 = header_node

    #with 2 pointers going at different speeds, if there is a loop within the linked list
    #the two will eventually meet up. If they start at same point, they will meet at the
    #same point later on.
    while pointer_2.next:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next.next
        if pointer_1 is pointer_2:
            break

    if pointer_2.next == None: #no meeting point
        return None

    #now suppose Fast runner had a head start of k meters on an n step lap. when will they
    #meet? they will meet K meters before the start of the next lap. (fast runner would have made
    #k + 2(n-k) steps, including its head start, and slow runner would have made n - k steps)
    #both will be k steps before the start of the loop
#     Now, going back to the problem, when Fast Runner (n2) and Slow Runner (n1) are moving
# around our circular linked list, n2 will have a head start on the loop when n1 enters. Speci!-
# cally, it will have a head start of k, where k is the number of nodes before the loop. Since n2
# has a head start of k nodes, n1 and n2 will meet k nodes before the start of the loop.
# So, we now know the following:
# 1. Head is k nodes from LoopStart (by de!nition).
# 2. MeetingPoint for n1 and n2 is k nodes from LoopStart (as shown above).
# Thus, if we move n1 back to Head and keep n2 at MeetingPoint, and move them both at the
# same pace, they will meet at LoopStart.
    pointer_1 = header_node
    while pointer_1 is not pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next

    return pointer_2


if __name__ == '__main__':
    header = Node(chr(97)) #'a'

    itr_node = header
    for i in range(9):
        if i == 5:
            test_node = itr_node
        if i == 8:
            itr_node.next = test_node #make circle loop 
        else:
            itr_node.next = Node(chr(98+i))
            itr_node = itr_node.next

    itr_node = header
    test_node = None
    for i in range(10):
        if i == 5:
            test_node = itr_node
        if itr_node is test_node:
            print 'header', itr_node.data
        else:
            print itr_node.data
        itr_node = itr_node.next

    result_node = get_head_of_circular_list(header)
    print "head of circular list: ",result_node.data


