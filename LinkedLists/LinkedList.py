class Node:
    def __init__(self,data=None):
        self.next = None
        self.data = data

    def __repr__(self):
        return "%s(%d)" % (self.__class__, self.data)

    def __str__(self):
        return "Data = %s" % (self.data)

class LinkedList:
    def __init__(self,node=None):
        self.header = node

    def __iter__(self):
        current = self.header
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        list_string = ""
        if self.header:
            itr = self.header
            while itr:
                list_string += str(itr.data) + " "
                itr = itr.next
        else:
            list_string += "No nodes exist within this linked list"
        return list_string

    def add_node(self,node):
        if self.header:
            itr = self.header
            while itr.next:
                itr = itr.next
            itr.next = node
        else:
            self.header = node
            
    """
    Remove all nodes with the corresponding value
    """
    def remove_value(self,value):
        prev_itr = None
        if self.header:
            itr = self.header
            while itr:
                if itr.data == value:
                    if itr.next:
                        if prev_itr:
                            prev_itr.next = itr.next
                        else:
                            self.header = itr.next
                    else:
                        if prev_itr:
                            prev_itr.next = None
                        else:
                            self.header = None
                else:
                    prev_itr = itr
                itr = itr.next

if __name__ == '__main__':
    node = Node()
    print node
