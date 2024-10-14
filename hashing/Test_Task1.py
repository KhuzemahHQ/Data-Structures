from multiprocessing import Process, Value
from Task1_B import Chaining
import time
import random
import sys


def test(lines, queries, score):
    start_time = time.time()
    print("Testing Insert")
    mytable = Chaining(202001)
    for i in lines:
        mytable.insert_word(i)

    if mytable.hash_table != None:
        print(f'Insertion Passed!')
        score.value += 5
    else:
        print("Insertion failed")

    print("Testing Lookup")
    lookup = True
    for i in lines:
        if mytable.lookup_word(i) == False or mytable.lookup_word(i) != i:
            print("Lookup Failed")
            lookup = False
            break
    if lookup == True:
        score.value += 10
        print("Lookup Passed!")

    print("Testing Delete")

    for i in queries:
        mytable.delete_word(i)

    lookup = True
    for i in queries:
        if mytable.lookup_word(i) != False:
            print("Delete failed")
            lookup = False
            break
    if lookup == True:
        score.value += 15
        print("Delete passed!")
    end_time = time.time()
    tot_time = end_time-start_time
    print("Total time taken : ", tot_time, " seconds")


if __name__ == '__main__':
    with open("testwords.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    print("Total number of words being inserted: ", len(lines))
    queries = []
    for i in lines:
        x = random.randint(0, sys.maxsize) % 5
        if x < 2:
            queries.append(i)
    score = Value('d', 0.0)
    p1 = Process(target=test, args=(
        lines, queries, score), name='test_chaining')
    p1.start()
    p1.join(timeout=17)
    p1.terminate()
    if p1.exitcode is None:
        print(f'Oops, {p1} timed out!')
    print("your score is: ", score.value)
