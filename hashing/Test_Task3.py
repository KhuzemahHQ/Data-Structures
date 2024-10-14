from Task3 import StorePasswords
from Task1_A import get_hashcode


def test():
    score = 0
    mytable = StorePasswords(10000)
    
    print("Testing Store Password")
    mytable.store_password("Muhammad", ("baseball","123456","trustno1",1))
    mytable.store_password("Amna", ("abc123","dragon","letmein",0))
    mytable.store_password("Faizan", ("sunshine","football","qwerty",2))
    mytable.store_password("Fatimah", ("shadow","password","welcome",1))
    mytable.store_password("Shahmir", ("princess","qwerty123","superman",1))
    mytable.store_password("Aden", ("whatever","freedom","1q2w3e",2))
    mytable.store_password("Ahmad", ("111111","donald","charlie",0))
    mytable.store_password("Emaan", ("liverpool1","ninja","admin",0))
    mytable.store_password("Maryam", ("!@#$%^&*","starwars","arsenal",2))
    mytable.store_password("Usama", ("login","zaq1zaq1","iloveyou",2))
    
    test_insert = mytable.all_users["Aden"]
    if get_hashcode("whatever") in test_insert:
        score += 2
    else:
        print('Store Password Failed!')
        return
    if get_hashcode("freedom") in test_insert:
        score += 2
    else:
        print('Store Password Failed!')
        return
    if get_hashcode("1q2w3e") in test_insert:
        score += 2
    else:
        print('Store Password Failed!')
        return
    len_three = False
    for value_list in mytable.all_users.values():
        if len(value_list) == 3:
            len_three = True
        else:
            print('Store Password Failed!')
            return
    if len_three == True:
        score += 3
    else:
        print('Store Password Failed!')
        return
    print('Store Password Passed!')


    print("Testing Find Password")
    if mytable.find_password("donald") == ("Ahmad", "hack_alert"):
        score += 3
    else:
        print('Find Password Failed!')
        return
    if mytable.find_password("123456") == ("Muhammad", "successful_login"):
        score += 3
    else:
        print('Find Password Failed!')
        return
    if mytable.find_password("champ") == ("login_failed"):
        score += 3
    else:
        print('Find Password Failed!')
        return
    print('Find Password Passed!')


    print("Testing Update Password")
    if mytable.update_password("!@#$%^&*", "here123") == ("Maryam", "hack_alert"):
        score += 3
    else:
        print('Update Password Failed!')
        return
    if mytable.update_password("abc123", "helloworld") == ("Amna", "successful_password_update"):
        if mytable.find_password("helloworld") == ("Amna", "successful_login"):
            score += 2
        else:
            print('Update Password Failed!')
            return
        if mytable.find_password("abc123") == ("login_failed"):
            score += 2
        else:
            print('Update Password Failed!')
            return
        
        test_update = mytable.all_users["Amna"]
        if get_hashcode("abc123") not in test_update:
            score += 1
        else:
            print('Update Password Failed!')
            return
        if get_hashcode("helloworld") in test_update:
            score += 1
        else:
            print('Store Password Failed!')
            return
    else:
        print('Update Password Failed!')
        return
    if mytable.update_password("bluesea", "whynot") == ("login_failed"):
        score += 3
    else:
        print('Update Password Failed!')
        return
    print('Update Password Passed!')
    
    return score

if __name__ == '__main__':
    score = test()
    print("Total Score:", score, "/30")
