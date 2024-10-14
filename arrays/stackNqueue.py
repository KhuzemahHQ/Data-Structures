from linkedlist import LinkedList, Node
# Assignment 1-Part 2
# Linkedlist-based Stacks and Queues

# Implementation of Stack
class Stack(LinkedList): 
    # Initializing the stack
    def __init__(self, cap):
        self.capacity = cap
        LinkedList.__init__(self)
    
    # To-do Function 1
    # Make sure that the stack does not go beyond its capacity
    def push(self, data):
        if self.get_length() >= self.capacity:
            return None
        self.insert_at_head(data)
    
    # To-do Function 2
    def pop(self):
        if self.is_empty():
            return None
        self.delete_head()
    
    # To-do Function 3
    def top(self):
        return self.get_head()

# Implementation of Queue
class Queue(LinkedList): 
    # Initializing the queue
    def __init__(self, cap):
        self.capacity = cap
        LinkedList.__init__(self)
    
    # To-do Function 4
    # Make sure that the queue does not go beyond its capacity 
    def enqueue(self, data):
        if self.get_length() >= self.capacity:
            return None
        self.insert_at_tail(data)
    
    # To-do Function 5
    def dequeue(self):
        if self.is_empty():
            return None
        self.delete_head()
    
    # To-do Function 6
    def get_front(self):
        return self.get_head()
    
    # To-do Function 7
    def get_rear(self):
        return self.get_tail()

# Testing Area ---

# You can create a class Linked List object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
def main():
    pass
    # Create an object here to test the functions.
    


# Comment out the line below before running your test files.
#main()