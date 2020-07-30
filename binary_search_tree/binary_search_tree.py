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

        # if the input is less than the current value
        if value < self.value:

            # if there is no left child
            if not self.left:

                # insert it!
                self.left = BSTNode(value)
            
            # if there is already a left child
            else:

                # repeat the process
                self.left.insert(value)

        # if the input is more than or equal to the current value
        elif value >= self.value:

            # if there is no right child
            if not self.right:

                # the input is now the right child!
                self.right = BSTNode(value)

            # if there is already a right child
            else:

                # repeat the process
                self.right.insert(value)


    def contains(self, target):

        """Returns true if the tree contains the value.
        False if it does not.
        """

        # if the input is the current value        
        if target == self.value:

            # it exists in the BST!
            return True

        # otherwise if the the input is less than the current value
        elif target < self.value:

            # if there is no left child
            if not self.left:

                # it ain't in this tree
                return False

            # if there is a left child
            else:

                # recursion (the left child is the new tree root, see if target is in it)
                return self.left.contains(target)

        # otherwise if the input is greater than or equal to the target
        elif target >= self.value:

            # if there is no right child
            if not self.right:

                # it ain't in this tree
                return False

            # if there is a right child
            else:

                # recursion (the right child is the new tree root, see if target is in it)
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):

        # the current value is the max, for now
        current_max = self.value

        # if there's no value larger than the current value
        if not self.right:

            # than this value is the biggest :)
            return current_max

        # if there is a value larger than the current value
        elif self.right:

            # set the root of the tree to the right child and run 
            # the new current_max through the function
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        # call the function on the input value
        fn(self.value)

        # if there is a left child
        if self.left:

            # run the function through again 
            # with the left child as the root of the tree
            self.left.for_each(fn)

        # if there is a right child
        if self.right:

            # run the function through again 
            # with the right child as the root of the tree
            self.right.for_each(fn)
            
    def delete(self, value):
        # search like we did in 'contains()'
        if value == self.value:
            # if no children
            if not self.left and not self.right:
                self.value = None
            # if two children
            elif self.left and self.right:
                self.value = self.right
            # if one child
            elif self.left and not self.right:
                self.value = self.left
            elif self.right and not self.left:
                self.value = self.right
            # if node at bottom level
                # update parent left/right = NOne
            # if node has only child
                # parent.left/right = node.left/right child
            # if node has two children
                # if larger child becomes the parent of its sibling
        elif value < self.value:
            return self.left.delete(value)
            pass
        elif value >= self.value:
            return self.right.delete(value)
   


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self:
            if self.left:
                # go left with recursion!
                self.left.in_order_print()
            if self.right:
                # go right with recursion 
                self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # route finding
        # don't want to search deep. don't want to go down one road 
        # forever. 

        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # a maze is a good example
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
