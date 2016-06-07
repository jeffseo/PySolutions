"""
2.1
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

"""

from LinkedList import Node, LinkedList
import random

def remove_duplicates(linked_list):
    tracker = {}
    for i in linked_list:
        if i.data not in tracker:
            tracker[i.data] = 1
        else:
            tracker[i.data] += 1
    print tracker
    for i in linked_list:
        if tracker[i.data] > 1:
            linked_list.remove_value(i.data)
    return linked_list

def remove_duplicates_node_only(node):
    tracker = {}
    previous_node = None
    itr_node = node
    while itr_node:
        if itr_node.data in tracker:
            previous_itr_node.next = itr_node.next
        else:
            tracker[itr_node.data] = 1
            previous_itr_node = itr_node
        itr_node = itr_node.next

"""
without buffer
"""
def remove_duplicates_node_only_v2(node):
    current_node = node
    while current_node:
        previous_node = current_node
        runner_node = current_node.next
        while runner_node:
            if runner_node.data == current_node.data:
                previous_node.next = runner_node.next
            else:
                previous_node = runner_node
            runner_node = runner_node.next

if __name__ == '__main__':
    # Using my lined list
    test_list = LinkedList()
    for i in range(10):
        node = Node(random.randint(0,10))
        test_list.add_node(node)
    print test_list
    remove_duplicates(test_list)
    print test_list

    # Using only nodes
    head_node = Node(0)
    itr_node = head_node
    for i in range(10):
        itr_node.next = Node(random.randint(0,10))
        itr_node = itr_node.next

    print 'Before removal'
    itr_node = head_node
    while itr_node:
        print itr_node.data
        itr_node = itr_node.next

    remove_duplicates_node_only(head_node)

    print 'after removal'
    itr_node = head_node
    while itr_node:
        print itr_node.data
        itr_node = itr_node.next
