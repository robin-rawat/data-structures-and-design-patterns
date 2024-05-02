"""
Heap is binary tree data structures which satisfies this condition : the parent node should be max or min of its leaves.
application : priority queue
"""

#max heap : binary tree with max element as root

class MaxHeap:
    array = []
    length = 0

    @classmethod
    def heapify(cls, node_index):
        max = node_index
        left = 2*node_index + 1
        right = 2*node_index + 2

        if left < cls.length and cls.array[max] < cls.array[left]:
            max = left
        if right < cls.length and cls.array[max] < cls.array[right]:
            max = right
        if max != node_index:
            cls.array[max], cls.array[node_index] = cls.array[node_index], cls.array[max]

    #used in heap sorting
    @classmethod
    def reverse_heapify(cls, node_index, last):
        max = node_index
        left = 2*node_index + 1
        right = 2*node_index + 2
        if left < last and cls.array[max] < cls.array[left]:
            max = left
        if right < last and cls.array[max] < cls.array[right]:
            max = right
        if max != node_index:
            cls.array[max], cls.array[node_index] = cls.array[node_index], cls.array[max]
            cls.reverse_heapify(max, last)

    @classmethod
    def get_nodes_length(cls):
        cls.length = len(cls.array)
        #for a array of length l, count of nodes with leafs will be = (l//2 - 1)
        return cls.length//2 - 1

    @classmethod
    def make_heap_from_array(cls, array = []):
        cls.array.extend(array)
        nodes = cls.get_nodes_length()
        #we want to sort first from the end nodes and progress upward to root
        for node_index in range(nodes, -1, -1):
            cls.heapify(node_index)
        return cls.array
    
    @classmethod
    def insert_in_heap(cls, element):
        cls.array.append(element)
        nodes = cls.get_nodes_length()
        for node_index in range(nodes, -1, -1):
            cls.heapify(node_index)
        return cls.array

    @classmethod
    def pop_max(cls):
        max = cls.array.pop(0)
        cls.make_heap_from_array()
        return max
    
    @classmethod
    def heap_sort(cls, array = []):
        cls.array.extend(array)
        nodes = cls.get_nodes_length()
        for node_index in range(nodes, -1, -1):
            cls.heapify(node_index)
        for last in range(cls.length-1, 0, -1):
            #Now we need to exchange first and last element of array
            cls.array[last], cls.array[0] = cls.array[0], cls.array[last]
            cls.reverse_heapify(0, last)
        return cls.array

array = [31,8,3,9,10,4,23,12,1,2,5,17]
#worst_complexity = log(n)
print(MaxHeap.make_heap_from_array(array))
print(MaxHeap.insert_in_heap(11))
print(MaxHeap.pop_max())
print(MaxHeap.array)
print(MaxHeap.heap_sort())