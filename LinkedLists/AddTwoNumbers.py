"""
2.4
You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1's digit is at the head of
the list. Write a function that adds the two numbers and returns the sum as a linked
list.
EXAMPLE
Input: (3 -> 1 -> 5), (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
"""
from LinkedList import Node
import random

"""
self-note Python call by object reference
http://www.informit.com/articles/article.aspx?p=2355856&seqNum=4
The only difference between a parameter variable and a local variable is that Python initializes 
the parameter variable with the corresponding argument provided by the calling code. We refer to 
this approach as call by object reference. (It is more commonly known as call by value, where the 
value is always an object reference-not the object's value.) One consequence of this approach is 
that if a parameter variable refers to a mutable object and you change that object's value within 
a function, then this also changes the object's value in the calling code (because it is the same object).

Important! If you change the object's value (if it is MUTABLE) within a function, 
then this also changes the object's value in the calling code

"""
def add_two_list(list_1,list_2):
    sum_1 = 0
    sum_2 = 0
    power = 0
    while list_1:
        sum_1 += (list_1.data * 10**power) 
        power += 1
        list_1 = list_1.next

    power = 0
    while list_2:
        sum_2 += (list_2.data * 10**power)
        power += 1
        list_2 = list_2.next

    total_sum = sum_1 + sum_2
    print sum_1, sum_2, total_sum

    itr = None
    for i in str(total_sum)[::-1]:
        if itr:
            itr.next = Node(i)
            itr = itr.next
        else:
            header = Node(i)
            itr = header
    return header

def add_two_list_recursive(list_1,list_2,carry=0):
    if not list_1 and not list_2:
        if carry > 0:
            return Node(carry)
        return None
    else:
        value = carry
        result_node = Node()
        if list_1:
            value += list_1.data
        if list_2:
            value += list_2.data
        if value >= 10:
            carry = 1
        else:
            carry = 0
        result_node.data = value % 10
        next_node = add_two_list_recursive(list_1.next,list_2.next,carry)
        result_node.next = next_node
        return result_node

if __name__ == '__main__':
    header = Node(random.randint(0,9))

    itr_node = header
    for i in range(2):
        itr_node.next = Node(random.randint(0,9))
        itr_node = itr_node.next

    itr_node = header
    while itr_node:
        print itr_node.data
        itr_node = itr_node.next

    print "iterative"
    node = add_two_list(header,header)

    itr_node = node
    while itr_node:
        print itr_node.data
        itr_node = itr_node.next

    print "recursive"
    node2 = add_two_list_recursive(header,header)

    itr_node = node2
    while itr_node:
        print itr_node.data
        itr_node = itr_node.next