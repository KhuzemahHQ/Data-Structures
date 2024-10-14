# Assignment 1-Part 1
# Linked Lists

# Single Node Class
from re import X


class Node:
    def __init__(self, data):
        self.data = data  # Assign data to node
        self.next = None  # Node initially does not point to any other node
  
# Linked List class
class LinkedList:
    # Initializing the linked list object. Head points to None.
    def __init__(self):
        self.head = None

    # Already provided
    def print_list(self):
        traverse = self.head
        LinkedList = []
        while(traverse):
            LinkedList.append(traverse.data)
            traverse = traverse.next
        return LinkedList
    
    # To-do Function 1
    # This function takes O(1)
    def get_head(self):
        if self.head == None:
            return None
        return (self.head).data
    
    # To-do Function 2
    # This function takes O(n)
    def get_tail(self):
        if self.head == None:
            return None
        x = self.head
        while x.next != None:
            x = x.next
        return x.data

    # To-do Function 3
    # This function takes O(1)
    def is_empty(self):
        if self.head == None:
            return True
        return False
    
    # To-do Function 4
    # This function takes O(1)
    def insert_at_head(self, data):
        x = Node(data)
        y = self.head
        x.next = y
        self.head = x

    # To-do Function 5
    # This function takes O(n)
    def insert_at_tail(self, data):
        x = Node(data)
        if self.head == None:
            self.head = x
        else:
            y = self.head
            while y.next != None:
                y=y.next
            y.next = x
        
    # To-do Function 6
    # Assume both the node to be inserted after and before exist in the right order in the test set
    # This function takes O(n)
    def insert_in_between(self, data, after, before):
        x = Node(data)
        y = self.head
        while y.data != after:
            y=y.next
        x.next = y.next
        y.next = x
    
    # To-do Function 7
    # This function takes O(1)
    def delete_head(self):
        self.head = (self.head).next
             
    # To-do Function 8
    # This function takes O(n)
    def delete_tail(self):
        y = self.head
        if y == None:
            return 
        elif y.next == None:
            self.head = None
            return 
        while (y.next).next != None:
            y=y.next
        y.next = None     
            
    # To-do Function 9
    # This function takes O(n)
    def delete_any(self, data):
        x = self.head
        if x.data == data:
            self.head = (self.head).next
            return
        y = None
        while x.data != data:
            y = x
            x=x.next
        y.next = x.next
        
    # To-do Function 10
    # This function takes O(n)
    def get_length(self):
        if self.head == None:
            return 0
        counter = 1
        x = self.head
        while x.next != None:
            x=x.next
            counter+=1
        return counter
    
    # To-do Function 11
    # This function takes O(n)
    def get_element(self, data):
        x=self.head
        while x.next != None:
            if x.data == data:
                return data
            x=x.next
        return False
    
    # To-do Function 12
    # This function takes O(n)
    def reverse_list(self):
        previous = None
        current = self.head
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            self.head = previous

# Testing Area ---

# You can create a class Linked List object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
def main():
    # Create an object here to test the functions.
    test_list = LinkedList()
    # Write code here

    print(test_list.print_list())


# Comment out the line below before running your test files.
#main()

# How can the time complexity of operations of the Linked List that you have implemented be improved?
# get_tail() and insert_at_tail() can be improved by adding a tail poniter to the Linked List
# delete_tail() can be improved by using a doubly linked list