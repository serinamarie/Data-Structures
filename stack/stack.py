"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from linkedlistclass import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        
    
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1
    
#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.remove_tail()



# We have to shift other elements around when using an array, 
# which can be computationally expensive. Changes to a linked list only affect
# a few elements (nodes) in contrast. Drawbacks on a singly linked list for a stack are that we
# need to iterate through the top of the stack down to the bottom if we want 
# to remove something we added long ago.