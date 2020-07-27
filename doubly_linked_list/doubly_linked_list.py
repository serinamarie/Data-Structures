
class ListNode:

    """Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    """

    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):	
        if self.prev:	
            self.prev.next = self.next	
        if self.next:	
            self.next.prev = self.prev
            

class DoublyLinkedList:

    """Our doubly-linked list class. It holds references to 
    the list's head and tail nodes.
    """

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):

        """Returns the length of the list"""

        return self.length
    

    def add_to_head(self, value):

        """Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly.
        """

        # wrap given value in a ListNode with its 'next' pointing
        # to the current head
        new_node = ListNode(value, next=self.head)

        # increment
        self.length += 1

        # if empty DLL
        if self.head is None and self.tail is None:

            # the new node is now the head and the tail!
            self.head = new_node
            self.tail = new_node
    
        else: 

            # have the current head's 'prev' pointing to the new node
            self.head.prev = new_node

            # then sets the new node to now be the head
            self.head = new_node

 
    def remove_from_head(self):

        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """

        # decrement
        self.length -= 1

        # if empty DLL
        if self.head is None and self.tail is None:

            return None
        
        else: 

            # store head value before removal
            old_head = self.head.value

            # if the DLL is of length 1
            if self.head == self.tail:

                self.head = None
                self.tail = None

            else:

                # the value after the head is now the new head!
                self.head = self.head.next

            # take a look at our removed head
            return old_head
  
    
    def add_to_tail(self, value):

        """Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly.
        """

        # wrap given value in a ListNode with its 'prev' pointing
        # to the current tail
        new_node = ListNode(value, prev=self.tail)

        # increment
        self.length += 1

        # if empty DLL
        if self.head is None and self.tail is None:

            # the new node is now the head and the tail!
            self.head = new_node
            self.tail = new_node
    
        else: 

            # have the current tail's 'next' pointing to the new node
            self.tail.next = new_node

            # then set the new node to now be the tail
            self.tail = new_node

            
    def remove_from_tail(self):

        """Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """

        # decrement
        self.length -= 1

        # if empty DLL
        if self.head is None and self.tail is None:

            return
        
        else: 

            # store tail value before removal
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
            

    def move_to_front(self, node):

        """Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        """

        # store node for use before removal
        input_node = node.value

        # if the node is the head, leave the head alone!
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

        # add the stored input_node value to the head 
        self.add_to_head(input_node)
       

    def move_to_end(self, node):
 
        """Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        """

        # store our node for future use before removal
        input_node = node.value

        # if node is already the tail, leave the tail alone!
        if node == self.tail:

            return None

        # if the node is the head
        elif node == self.head:

            # remove it from the head with our function
            self.remove_from_head()
        
        # if neither head nor tail
        else:

            # remove it
            node.delete()

            # decrement
            self.length -= 1

        # add the stored input_node value to the tail 
        self.add_to_tail(input_node)
        

    def delete(self, node):

        """Deletes the input node from the List, preserving the 
        order of the other elements of the List.
        """

        # if empty DLL
        if not self.head and not self.tail:

            return

        # decrement if not empty
        self.length -= 1

        # if DLL of length 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
 
        # if the node is the tail
        if self.tail == node:     

            # turn the node before the tail into the new tail      
            self.tail = self.tail.prev

        # if the node is the head
        elif self.head == node:

            # turn the node after the head into the new head
            self.head = self.head.next
        
        # then remove the node
        node.delete()
  

    def get_max(self):

        """Finds and returns the maximum value of all the nodes 
        in the List.
        """

        # if empty DLL, ignore
        if not self.head:

            return

        # start with the head as the current value
        current = self.head

        # the current node is the maximum, for now
        maximum = current.value

        # while we can continue to iterate
        while current:

            # if the current node is greater than the max
            if current.value > maximum:

                # then this node becomes the new maximum!
                maximum = current.value

            # go to the next value (it it's None, the loop will end)
            current = current.next

        # once all values have been checked, return the maximum value
        return maximum
