# Priority Queue
# Priority queue “owns” a heap as instance variable
# We use heap operations on the heap object to implement all priority queue operations.

from Heap import Heap

class PriorityQueue: # Comments indicate what methods the Heap class must have
    def __init__(self):
        self.queue_heap = Heap()

    def insert(self, item):
        """Put a new item in the queue"""
        self.queue_heap.insert(item) # insert

    def get_max(self):
        """Return the max item in the queue"""
        return self.queue_heap.get_max() # get_max

    def remove_max(self):
        """Return and remove the max item from the queue"""
        return self.queue_heap.remove_max() # remove_max

    def get_size(self):
        """Return the size"""
        return self.queue_heap.get_size() # get_size

    def is_empty(self):
        """Return true if the queue is empty"""
        return self.queue_heap.is_empty() # is_empty

    def __str__(self):
        return self.queue_heap.__str__() # __str__
