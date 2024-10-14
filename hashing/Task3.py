from Task2 import LinearProbing
from Task1_A import get_hashcode, div_compression

class StorePasswords(LinearProbing):
    def __init__(self, capacity):
        self.password_table = LinearProbing(capacity)
        self.all_users = {}
    
    def store_password(self, username, password_tuple): 
        '''
        Arguments:
        username: String e.g. "Ali"
        password_tuple: Tuple e.g. ("honeyword1", "true_password", "honeyword2", 1)
                       where last index will indicate the index of the true password.
        
        Returns: Nothing
        '''
        index = password_tuple[-1]
        self.all_users[username] = []

        for i in range(3):
            hash = get_hashcode(password_tuple[i])
            v = password_tuple[i]
            if i == index:
                hw = False
            else:
                hw = True
            self.all_users[username].append(hash)
            self.password_table.insert_word(v,hw)
            
    
    def find_password(self, password):
        '''
        Arguments:
        password: String 
        
        Returns: Tuple
        If the password is not found: (“login_failed”)
        If the password is the true password: (username, “successful_login”)
        If the password is a honeyword: (username, “hack_alert”)
        '''
        result = self.password_table.lookup_word(password)

        if result is None:
            return ("login_failed")

        else:
            hash = get_hashcode(password)
            for key in self.all_users.keys():
                if hash in self.all_users[key]:
                    username = key
            if  result.honeyword == True:
                return (username, "hack_alert")
            elif result.honeyword == False:
                return (username, "successful_login")

    
    def update_password(self, old_password, new_password):
        '''
        Arguments:
        old_password: String 
        new_password: String 
        
        Returns: Tuple
        If the password is not found: (“login_failed”)
        If the password is the true password: (username, “successful_password_update”)
        If the password is a honeyword: (username, “hack_alert”)
        '''
        result = self.password_table.lookup_word(old_password)

        if result is None:
            return ("login_failed")

        else:
            hash = get_hashcode(old_password)
            for key in self.all_users.keys():
                if hash in self.all_users[key]:
                    username = key
            if  result.honeyword == True:
                return (username, "hack_alert")
            elif result.honeyword == False:
                self.password_table.delete_word(old_password)
                self.password_table.insert_word(new_password,False)
                new_hash = get_hashcode(new_password)
                self.all_users[username].remove(hash)
                self.all_users[username].append(new_hash)
                return (username, "successful_password_update")
    
