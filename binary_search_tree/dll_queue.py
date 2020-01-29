import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Queue (cue)
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Each element has a reference to both the next and the previous element. This is useful bc having a reference to the previous element can speed up some operations, like removing (“unlinking”) an element from a list or traversing the list in reverse order.
        
        # We are setting DoublyLinkedList to storage
        self.storage = DoublyLinkedList()

    # Enqueue - to add (an item of data awaiting processing) to a queue of such items.
    def enqueue(self, value):
        # We are adding, so set the size to += 1.
        self.size += 1
        # Return add_to_tail(value) because we add to the tail and remove from the head.
        return self.storage.add_to_tail(value)
        

    def dequeue(self):
        
        if self.size == 0:
            pass
        else:
            self.size -= 1
            return self.storage.remove_from_head()
        

    def len(self):
        return self.size