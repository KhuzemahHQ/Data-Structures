import random
import time
import sys
from Task2 import LinearProbing
from multiprocessing import Process, Value

def test(allWords, queries, score):
    start_time = time.time()
    
    myTable = LinearProbing(1000)
    
    print("Starting Tests")
    print("Testing Insert:")
    
    for word in allWords:
        myTable.insert_word(word, None)
        
    score.value += 10
    print("Insert Passed!")
    print("Testing Lookup:")
    
    for word in allWords:
        if not myTable.lookup_word(word):
            print("Failed")
            return 
        
        if myTable.lookup_word(word).value != word:
            print("Failed")
            return 
    
    score.value += 10
    
    print("Lookup Passed!")
    print("Testing Delete:")
    
    for i in range(len(queries)//2):
        myTable.delete_word(queries[i])
        
    for i in range(len(queries)//2):
        
        if myTable.lookup_word(queries[i]):
            print("Failed")
            return 
        
    score.value += 10
    
    for i in range(len(queries)//2, len(queries)):
        
        if not myTable.lookup_word(queries[i]):
            print("Failed")
            return
        
        if myTable.lookup_word(queries[i]).value != queries[i]:
            print("Failed")
            return 
    end_time = time.time()
    tot_time = end_time-start_time
    
    score.value += 10
    print("Delete Passed!")
    print("Total time taken : ", tot_time, " seconds")
    
    
if __name__ == '__main__':
    allWords = []
    with open("words.txt") as file:
        allWords = [line.rstrip() for line in file]
    file.close()
    print("Total number of words being inserted:", allWords)
    queries = []
    for word in allWords:
        x = random.randint(0, 5)
        if (x < 2):
            queries.append(word)
    score = Value('d', 0.0)
    p1 = Process(target=test, args=(
        allWords, queries, score), name='test_linearprobing')
    p1.start()
    p1.join(timeout=40)
    p1.terminate()
    if p1.exitcode is None:
        print(f'Oops, {p1} timed out!')
    print("Total Score:", int(score.value), "/40")