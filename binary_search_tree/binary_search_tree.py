import sys
sys.path.append('/queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# BINARY SEARCH TREE NOTES:
# DOG, DAD, DWELL
# BASE = DOG
# DAD WOULD GO TO THE LEFT BECAUSE IT'S LESS(<) THAN DOG
# DWELL WOULD GO TO THE RIGHT BECAUSE IT'S GREATER(>) THAN DOG
# IF THERE IS ANOTHER DOG, IT WOULD GO TO THE RIGHT BECAUSE IT'S EQUAL TO DOG

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.queue = Queue()
        self.stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        # If the value is less(<) than than the value of the node being compared, go left.
        if value < self.value:
            # If left then insert the value in left.
            if self.left:
                self.left.insert(value)
            # Otherwise left is equal to the value of the BinarySearchTree
            else:
                self.left = BinarySearchTree(value)
        else:
            # If not right then right is equal to the value of the BinarySearchTree
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # Otherwise insert the value to right.
                self.right.insert(value)
            
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If target is equal to the self.value, then return True
        if target == self.value:
            return True
        # If target is less than the self.value
        if target < self.value:
            # And if self.left is NOT equal to None, then return self.left that contains the target.
            if self.left != None:
                return self.left.contains(target)
        if target >= self.value:
            if self.right != None:
                return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            # 
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Set 'cb' to self.value
        cb(self.value)
        if self.left != None and self.right != None:
            return (self.left.for_each(cb), self.right.for_each(cb))
        elif self.left != None and self.right == None:
            return self.left.for_each(cb)
        elif self.left == None and self.right != None:
            return self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # If node then print left node.
        if node:
            self.in_order_print(node.left)
            print('Node values:', node.value)
            
        # Then print the right node
            self.in_order_print(node.right)
            
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        self.queue.enqueue(self)
        while(self.queue.size > 0):
            node = self.queue.dequeue()
            if node.right:
                self.queue.enqueue(node.right)
            if node.left:
                self.queue.enqueue(node.left)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack.push(self)
        while(self.stack.size > 0):
            node = self.stack.pop()
            if node.left is not None:
                self.stack.push(node.left)
            if node.right is not None:
                self.stack.push(node.right)
            print(node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
