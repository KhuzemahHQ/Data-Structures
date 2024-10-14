from Task1_A import get_hashcode, div_compression


class TableItem:
    def __init__(self, k, v, hw):
        '''
        Arguments:
        k: Integer (Hash key)
        v: String
        hw: Bool (for Task2 = None, for Task3 = True/False)
        '''

        self.key = k
        self.value = v
        self.honeyword = hw


class LinearProbing(TableItem):
    def __init__(self, table_size):
        '''
        Arguments:
        table_size: Integer
        
        Class members:
        self.count = Integer (Counts the number of items in the Hashtable)
        self.table_size = Integer (The size of the hashtable)
        self.hash_table = List (Hashtable)
        '''
        self.count = 0
        self.table_size = table_size
        self.hash_table = [None for i in range(self.table_size)]

    def get_hash(self, value):
        '''
        Arguments:
        value: String

        Returns: 
        Compressed Hash Code: Integer

        Use functions from Task1_A.py here
        Essentially the same funciton you implemented in Task1_B.py
        '''
        hashcode = get_hashcode(value)
        hash = div_compression(hashcode,self.table_size)
        return hash

    def resize_table(self):
        '''
        Function called in insert_word() function.

        Choose resize factor of your choice. 
        This will determine the time you take to pass the tests so try different values.

        Returns: Nothing
        '''
        self.table_size *= 2
        temp_table = [None for i in range(self.table_size)]
        for element in self.hash_table:
            if element != None:
                new = self.get_hash(element.value)
                while temp_table[new] != None:
                    new += 1
                    if new >= self.table_size:
                        new -= self.table_size
                temp_table[new] = TableItem(new,element.value,element.honeyword)
        self.hash_table = temp_table

    def insert_word(self, value, honeyword_flag):
        '''
        Arguments:
        value: String
        honeyword_flag: Bool (for Task2 = None, for Task3 = True/False)

        Call resize() function here when loadfactor is high.
        Choose loadfactor of your choice. 
        This will determine the time you take to pass the tests so try different values.

        Returns: Nothing
        '''
        self.count += 1
        loadfactor = float(self.count/self.table_size)
        if loadfactor > 0.5:
            self.resize_table()
        hash = self.get_hash(value)
        while self.hash_table[hash] != None:
            hash += 1
            if hash >= self.table_size:
                hash -= self.table_size
        self.hash_table[hash] = TableItem(hash,value,honeyword_flag)

    def delete_word(self, value):
        '''
        Arguments:
        value: String

        Returns: Nothing
        '''
        hash = self.get_hash(value)
        while self.hash_table[hash] != None:
            if self.hash_table[hash].value == value:
                self.hash_table[hash].value = "deleted_flag"
                return
            hash += 1

    def lookup_word(self, value):
        '''
        Arguments:
        value: String

        Returns:
        if value found: TableItem()
        if value not found: None
        '''
        actual_hash = self.get_hash(value)
        hash = actual_hash
        while self.hash_table[hash] != None:
            if self.hash_table[hash].value == value:
                return self.hash_table[hash]
            hash += 1

        return None
