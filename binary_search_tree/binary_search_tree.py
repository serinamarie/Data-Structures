"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):

        '''Insert the given value into the tree'''

        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

        # # if a root with no children
        # if not self.left and not self.right:

        #     if value == self.value:
        #         self.value = value

        #     # if the input value is less than the current value
        #     elif value < self.value:

        #         # make the input value into the left child
        #         self.left = value

        #     # otherwise if the input value is greater than the current value
        #     elif value > self.value:

        #         # make the input value into the right child
        #         self.right = value
        
        # # if a root with a child
        # else:

        #     # begin with the root as the current value
        #     # (I call it the 'cursor' as a reminder that it only 
        #     # refers to our location in our search)
        #     cursor = self.value
        
        #     # while we have not reached a leaf (bottom of the tree)
        #     while self.left or self.right:

        #         # if the input value is less than the cursor
        #         if value < cursor:

        #             # move our cursor to the left (move down left)
        #             cursor = self.left

        #             # if that space is vacant
        #             if cursor == None:

        #                 # set the input value as our new left
        #                 self.left = value

        #         # if the input value is greater than the cursor
        #         elif value > cursor: 

        #             # move our cursor to the right (move down right)
        #             cursor = self.right

        #             # if the space is vacant
        #             if cursor == None:

        #                 # set the input value as our new right
        #                 self.right = value


    def contains(self, target):

        """Returns true if the tree contains the value.
        False if it does not.
        """

        # while the current value has children
        while self.left or self.right:

            # if the current value is either of the children
            if self.left == target or self.right == target:

                # exit the loop
                break

            # if the current value isn't either of the children
            else:

                #if the target is less than the current value 
                if target < self.value:

                    # make the left child the new current value
                    self.value = self.left

                # if the target is greater than the current value
                else:

                    # make the right child the new current value
                    self.value = self.right

        # now that the loop is broken, see if the target matches either child
        if target == self.left or target == self.right:

            # if so return True
            return True

        else:

            # otherwise return False
            return False
            


    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
