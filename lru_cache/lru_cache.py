from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # Setting the number of limit
        self.limit = limit
        
        # Set the storage to DoublyLinkedList()
        self.storage = DoublyLinkedList()
        
        # Setting the node to set because we don't know what the current number is.?
        self.node = 0
        
        #Set the cache
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache:
            self.storage.move_to_front(self.cache[key])
            return self.cache[key].value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # If the ket is in self.cache.
        if key in self.cache:
            # The node is equal to self.cache and a key is being passed in.
            node = self.cache[key]
            # The node.value is equal to value.
            node.value = value
            # Then we the self.cache[key] move to the front.
            self.storage.move_to_front(self.cache[key])
            # Now return node.value
            return node.value
        
        # If the length of the storage is greater(>) or equal to the limit.
        if len(self.storage) >= self.limit:
            # Then the tail is equal/set to the self.storage.tail
            tail = self.storage.tail
            # Now we use the remove_from_tail function
            self.storage.remove_from_tail()
            # Now we are looking for the oldest in the cache.
            for oldest in self.cache:
                # If we find it, then we want to delete it.
                if self.cache[oldest] == tail:
                    del self.cache[oldest]
                    break
        # Now we are adding to the head.        
        self.storage.add_to_head(value)
        # Then we store it.
        self.cache[key] = self.storage.head