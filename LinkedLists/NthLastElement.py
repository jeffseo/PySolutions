"""
2.2
Implement an algorithm to find the nth to last element of a singly linked list.

iterative solution:
use two pointers to the linked list. one pointer should point to the n-1 index from the beginning
if that pointer.next does not equal Null, increment both pointer
this allows the pointer thats not at n-1 to be at n from last 

"""

from LinkedList import Node
import random

def find_nth_to_last(node,n):
    ptr_1 = node
    ptr_2 = node

    for i in range(n-1):
        if ptr_2 == None:
            return None
        ptr_2 = ptr_2.next

    while ptr_2.next != None:
        ptr_2 = ptr_2.next
        ptr_1 = ptr_1.next
    else:
        print ptr_1.data
"""
We need a variable that will hold it's value across multiple recursive function calls. 
Any ideas? What about using a static variable? That's actually perfect - 
because a static variable by definition will hold it's value across many different 
function calls, because static variables are not stored in the same area of memory as local variables.
http://www.programmerinterview.com/index.php/data-structures/find-nth-to-last-element-in-a-linked-list/
"""
static_counter = 0
def find_nth_to_last_recursive(node,n):
    global static_counter
    if node == None:
        return
    find_nth_to_last_recursive(node.next,n)
    static_counter += 1
    if static_counter == n:
        print node.data

if __name__ == '__main__':
    header = Node(random.randint(0,10))
    itr_node = header
    for i in range(1,10):
        itr_node.next = Node(random.randint(0,10))
        itr_node = itr_node.next

    itr_node = header
    while itr_node:
        print itr_node.data
        itr_node = itr_node.next

    find_nth_to_last(header,5)
    find_nth_to_last_recursive(header,5)