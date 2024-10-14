# Linked Lists 

# Single Node Class
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None
  
# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        traverse = self.head
        LinkedList = []
        while(traverse):
            LinkedList.append(traverse.data)
            traverse = traverse.next
        return LinkedList
    
    def get_head(self):
        if self.head == None:
            return None
        return self.head.data
    
    def get_tail(self):
        if self.head == None:
            return self.head
        else:
            traverse = self.head
            while(traverse.next):
                traverse = traverse.next
            return traverse.data

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            traverse = self.head
            while(traverse.next):
                traverse = traverse.next
            traverse.next = new_node      
            new_node.next = None

    def insert_in_between(self, data, after, before):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:                                  
            traverse = self.head
            while(traverse.data != after):
                traverse = traverse.next
            new_node.next = traverse.next 
            traverse.next = new_node   
      
    def delete_head(self):
        del_node = self.head
        self.head = del_node.next
        del_node.next = None
             
    def delete_tail(self):
        traverse = self.head
        if traverse.next == None:
            self.head = None
        prev = Node("")
        while(traverse.next != None):
            prev = traverse
            traverse = traverse.next
        prev.next = None     
                               
    def delete_any(self, data):
        del_node = Node(data)
        traverse = self.head
        if traverse.data == del_node.data:
            self.delete_head()
        prev = Node("")
        while(traverse.data != del_node.data):
            prev = traverse
            traverse = traverse.next
        prev.next = traverse.next

    def get_length(self):
        length = 0
        traverse = self.head
        while(traverse):
            length = length + 1
            traverse = traverse.next
        return length
    
    def get_element(self, data):
        found = False
        found_node = Node(data)
        traverse = self.head
        while(traverse):
            if(traverse.data == found_node.data):
                return traverse.data
            traverse = traverse.next
        return found
        