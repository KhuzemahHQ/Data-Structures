class heapNode:
    def __init__(self, value, doc_title=None):
        self.value = value # The integer key of the node
        self.doc_title = doc_title # The node's document title (you'll understand this in Part 3) for a priority queue's implementation in Task 3. Set to None for Task 2
        
class minHeap:
    def __init__(self, cap):
        self.harr = [None] * cap # List of elements in the min-heap
        self.capacity = cap # Maximum possible size of the min-heap
        self.heap_size = 0 # Current number of elements in the min heap (elements of type None don't count)

    # return index of the parent of a node at index i
    def parent (self, i):
        # formula for parent_index = floor[(i-1)/2]
        return (i-1)//2

    # get index of left child of node at index i
    def get_left_child_index (self, i):
        # formula for left child's index = 2i + 1
        return (2*i)+1

    # get index of right child of node at index i
    def get_right_child_index (self, i):
        # formula for right child's index = 2i + 2
        return (2*i)+2

    # Returns the minimum node (node at root) from min heap
    def get_min (self):
        return self.harr[0]
    
    # remove minimum node (or root) from min heap
    def extract_min (self):
        result = self.get_min()
        self.harr[0] = self.harr[self.heap_size-1]
        self.harr[self.heap_size-1] = None
        self.heap_size -= 1
        self.percolate_down(0)
        return result

    # Decreases value of node at index i to new_val (assume new_val will always be smaller than value in harr[i])
    def decrease_node (self, i, new_val):
        self.harr[i].value = new_val
        self.percolate_up(i)

    # Deletes the node stored at index i
    def delete_node (self, i):
        if i > self.heap_size:
            return "Error: Index out of range!"
        if self.harr[i] == None:
            return 
        self.decrease_node(i, - float('inf'))
        self.extract_min()

    # Inserts a new node with value 'value'
    def insert_node (self, value, doc_title = None):
        if self.heap_size >= self.capacity:
            return "Error: The heap is at maximum capacity!"
        self.harr[self.heap_size] = heapNode(value, doc_title)
        self.percolate_up(self.heap_size) 
        self.heap_size += 1
        
    # Helper function to percolate_down after editing the heap
    def percolate_down(self, curr_index):
        # percolate down
        new = curr_index
        left_child = self.get_left_child_index(curr_index)
        right_child = self.get_right_child_index(curr_index)
        if right_child < self.heap_size and self.harr[right_child].value < self.harr[new].value:
            new = right_child
        if left_child < self.heap_size and self.harr[left_child].value < self.harr[new].value:
            new = left_child
        if new == curr_index:
            return
        else:
            self.harr[new] , self.harr[curr_index] = self.harr[curr_index] , self.harr[new]
            self.percolate_down(new)

    # Helper function to percolate_down after editing the heap
    def percolate_up(self, curr_index):
        while curr_index != 0 and self.harr[self.parent(curr_index)].value > self.harr[curr_index].value:
            self.harr[self.parent(curr_index)], self.harr[curr_index] = self.harr[curr_index], self.harr[self.parent(curr_index)]
            curr_index = self.parent(curr_index)