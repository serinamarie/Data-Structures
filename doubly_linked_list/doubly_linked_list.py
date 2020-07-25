"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):	
        if self.prev:	
            self.prev.next = self.next	
        if self.next:	
            self.next.prev = self.prev
            
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

            # add the new node before the head
            self.head.prev = new_node

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

            # add the new node to the tail
            self.tail.next = new_node

            # the new node is now the tail!
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

        # store node for use before removal
        input_node = node.value

        # if the node is the head, do nothing
        if node == self.head:
            return

        # if it's the tail
        elif node == self.tail:

            # remove it from the tail with a handy dandy function
            # the function will decrement the DLL 
            self.remove_from_tail()

        # if not the tail
        else:

            # remove it with our delete function
            node.delete()

            # we need to decrement it ourselves
            self.length -= 1

        # move it to the front 
        self.add_to_head(input_node)
       
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):

        # store our node for future use before removal
        input_node = node.value

        # if input node is already the tail, ignore
        if node == self.tail:
            return None

        # if it's the head
        elif node == self.head:

            # remove it from the head with our function
            self.remove_from_head()
        
        # if neither head nor tail
        else:

            # remove it with our delete function
            node.delete()

            # decrement
            self.length -= 1

        # move it to the front 
        self.add_to_tail(input_node)
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        # if empty DLL
        if not self.head and not self.tail:
            return

        # decrement if not empty
        self.length -= 1

        # if DLL of length 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
 
        # if the node is the tail, reset the tail
        if self.tail == node:           
            self.tail = self.tail.prev

        # if the node is the head, reset the head
        elif self.head == node:

            # if the head
            # make the next node the new head
            self.head = self.head.next
        
        # in the end we'll remove the node
        node.delete()
  


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):

        if not self.head:
            return

        current = self.head

        # the current node is the maximum, for now
        maximum = self.head.value


        # while we have a node to look at 
        while current:

            # if the current node is greater than the max
            if current.value > maximum:

                # the current value is the next maximum!
                maximum = current.value

            # go to the next value
            current = current.next

        # return the maximum value
        return maximum