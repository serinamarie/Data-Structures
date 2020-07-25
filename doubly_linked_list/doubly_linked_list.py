"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        # wrap given value in ListNode and insert it as new head
        new_node = ListNode(value, next=self.head)

        # increment
        self.length += 1

        # if empty DLL
        if self.head is None and self.tail is None:

            # the new node is now the head and the tail!
            self.head = new_node
            self.tail = new_node
    
        else: 

            # the new node is now the head!
            self.head = new_node

 
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        # decrement
        self.length -= 1

        # if empty DLL
        if self.head is None and self.tail is None:

            return None
        
        else: 

            # the current head is now the old_head
            old_head = self.head.value

            # if the DLL is of length 1
            if self.head == self.tail:

                self.head = None
                self.tail = None

            else:

                # the value before the head is now the new head!
                self.head = self.head.next

            # take a look at our removed head
            return old_head
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        
        # wrap given value in ListNode and insert it as new head
        new_node = ListNode(value, prev=self.tail)

        # increment
        self.length += 1

        # if empty DLL
        if self.head is None and self.tail is None:

            # the new node is now the head and the tail!
            self.head = new_node
            self.tail = new_node
    
        else: 

            # the new node is now the head!
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):

        # decrement
        self.length -= 1

        # if empty DLL
        if self.head is None and self.tail is None:

            return None
        
        else: 

            # the current tail is now the old_tail
            old_tail = self.tail.value

            # if the DLL is of length 1
            if self.head == self.tail:

                self.head = None
                self.tail = None

            else:

                # the value before the tail is now the new tail!
                self.tail = self.tail.prev

            # take a look at our removed tail
            return old_tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #
        # add to head(node.get_value())
        pass
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # look at what comes before this node, grab the next node (current node),
        # set to next node
        node.prev.next = node.next
        # look at what comes after node and set its previous pointer
        # equal to node's previous pointer
        node.next.prev = node.prev
        self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass