class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1


    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node

        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
    
    def remove_head(self):

        # empty LL
        if self.head is None:
            return None

        # list with 1 node
        elif self.length == 1:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        # list with +2 nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value
    
    def remove_tail(self):

        # if empty
        if not self.head:
            return None
        
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        
        else:

            # else set head to current
            current = self.head

            # then while there are nodes afterward
            while current.get_next() != self.tail:

                # change the current node to the next node, iterate
                current = current.get_next()
            # once the next node is none, set the current node to previous, and add none after it
            value = self.tail.get_value()
            current.set_next(None)

            # set that previous value to the new tail
            self.tail = current
            self.length -= 1

            # return the tail
            return value

    
    def contains(self, value):

        current_node = self.head

        while current_node is not None:

            # check if value input is same as current node
            if current_node.get_value() == value:
                return True
            # move on to next node
            current_node = current_node.get_next()
    
        # value not in LL
        return False

    def get_max(self):

        # empty list
        if self.head is None:
            return None

        # non-empty list
        # iterate through all elements
        current_node = self.head

        # set max to first node
        current_max = self.head.get_value()

        while current_node is not None:

            # search for higher values
            if current_node.get_value() > current_max:
                # set new max
                current_max = current_node.get_value()
            
            # move on to next node
            current_node = current_node.get_next()

        return current_max

    def find_middle(self):
        # Doing this in 1 pass, without using 'length' attribute
        mid_point = self.head
        end_point = self.head
        while end_point is not None and end_point.get_next() is not None:
            mid_point = mid_point.get_next()
            end_point = end_point.get_next().get_next()
        return mid_point.value

ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
ll.add_to_tail(5)

print(ll.find_middle())