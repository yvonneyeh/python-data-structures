class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        """Insert a new item in the heap"""
        (self.heap).append(item)
        self.up_heap()

    def get_max(self):
        """
        Return the max item in the heap
        Assume the max item exists.
        """
        return self.heap[0]

    def swap(self, i, j):
        """Swap the items at indices i and j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def remove_max(self):
        """Remove and return the max item in the heap"""
        last_index = len(self.heap) - 1
        if last_index == 0:
          return -1  #empty

        self.swap(1, last_index)
        max_value = self.heap.pop()
        self.heapify(1)
        return max_value
        # if len(self.heap) < 0 or len(self.heap) == 0:
        #   return None
        # self.swap(0, -1)
        # curr_max = (self.heap).pop()
        # # print(curr_max)
        # # print(self.heap[-1])
        # self.heapify(0)
        # return curr_max
        # last_index = len(self.heap) - 1
        # if last_index < 0:
        #   return -1
        # self.swap(0, last_index)
        # curr_max = self.heap.pop()
        # self.heapify(0)
        # return curr_max
        # if len(self.heap) > 1:
        #   self.swap(0, -1)
        #   self.heap.pop(-1)
        #   self.heapify(0)
        # else:
        #   return None

    def get_size(self):
        """Return the number of items in the heap"""
        return len(self.heap)

    def is_empty(self):
        """Return True if the heap is empty"""
        return len(self.heap) == 0

    # def heapify(self, i):
    #     """Restore max heap property starting at position i and working down recursively"""
    #     left_index = (2 * i) + 1
    #     right_index = (2 * i) + 2
    #     max_index = i

    #     if left_index < len(self.heap) and self.heap[left_index] > self.heap[i]:
    #       max_index = left_index
    #     if right_index < len(self.heap) and self.heap[right_index] > self.heap[i]:
    #       max_index = right_index

    #     if max_index is not i:
    #       self.swap(max_index, i)
    #       self.heapify(max_index)

    def heapify(self, i):
      last_index = len(self.heap) - 1
      left_index = (2 * i) + 1
      right_index = (2 * i) + 2
      temp_max_index = i

      if left_index <= last_index and self.heap[temp_max_index] < self.heap[left_index]:
        temp_max_index = left_index
      if right_index <= last_index and self.heap[temp_max_index] < self.heap[right_index]:
        temp_max_index = right_index

      if temp_max_index != i:
        self.swap(i, temp_max_index)
        self.heapify(temp_max_index)

    def up_heap(self):
        """
        Fix up relations between child and parent in order to
        restore heap ordering
        """
        curr_index = len(self.heap) - 1

        while curr_index > 0:
          parent_index = (curr_index - 1) // 2

          if self.heap[curr_index] > self.heap[parent_index]:
            self.swap(parent_index, curr_index)
            curr_index = parent_index
          else:
            break

    def __str__(self):
        return str(self.heap)

class PriorityQueue:
    def __init__(self):
        self.queue_heap = Heap()

    def insert(self, item):
        """Put a new item in the queue"""
        self.queue_heap.insert(item)

    def get_max(self):
        """Return the max item in the queue"""
        return self.queue_heap.get_max()

    def remove_max(self):
        """Return and remove the max item from the queue"""
        return self.queue_heap.remove_max()

    def get_size(self):
        """Return the size"""
        return self.queue_heap.get_size()

    def is_empty(self):
        """Return true if the queue is empty"""
        return self.queue_heap.is_empty()

    def __str__(self):
        return self.queue_heap.__str__()

my_pq = PriorityQueue()
my_pq.insert(100)
# print(my_pq)
my_pq.insert(10)
# print(my_pq)
my_pq.insert(40)
# print(my_pq)
my_pq.insert(3000)
# print(my_pq)
my_pq.insert(30)
# print(my_pq)
my_pq.insert(50)
# print(my_pq)
print(my_pq.get_max())
print(my_pq)
print("====")
print(my_pq.remove_max())
print(my_pq)
print(my_pq.remove_max())
print(my_pq)
print(my_pq.remove_max())
print(my_pq)
