from Task1_A import get_hashcode, div_compression
from LinkedList import LinkedList

class Chaining:
    def __init__(self, table_size):
        '''
        Arguments:
        table_size: Integer
        '''
        
        self.table_size = table_size
        self.hash_table = [LinkedList() for i in range(self.table_size)]

    def get_hash(self, value):
        '''
        Arguments:
        value: String
        
        Returns: 
        Compressed Hash Code: Integer
        
        Use functions from Task1_A.py here
        '''
        hashcode = get_hashcode(value)
        hash = div_compression(hashcode,self.table_size)
        return hash

    def insert_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns: Nothing
        '''
        hash = self.get_hash(value)
        self.hash_table[hash].insert_at_head(value)

    def delete_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns: Nothing
        '''
        hash = self.get_hash(value)
        self.hash_table[hash].delete_any(value)


    def lookup_word(self, value):
        '''
        Arguments:
        value: String
        
        Returns:
        if value is found: the value (String)
        if value is not found: False
        '''
        hash = self.get_hash(value)
        if self.hash_table[hash].get_length() == 0:
            return False
        else:
            return self.hash_table[hash].get_element(value)
