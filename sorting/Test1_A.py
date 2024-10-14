from Part1_A import merge_sort
import random

def sorting_test(main_list, score):
    print("Testing Merge Sort on 1000 lists")

    sorted_main_list = []
    for i in main_list:
        sorted_main_list.append(sorted(i))
    
    result_list = []
    for k in main_list:
        result_list.append(merge_sort(k))

    i=0
    check = True
    while i < len(sorted_main_list):
        if result_list[i] != sorted_main_list[i]:
            print()
            print("Merge Sort Failed!")
            print()
            check = False
            return 0
        i+=1
    if check == True:
        print()
        print("Merge Sort Passed!")
        print() 
        score += 10
    return score


if __name__ == '__main__':
    main_list  = []
    j=0
    while j < 1000:
        randomlist = []
        for i in range(random.randint(0,1000)):
            n = random.randint(1,100)
            randomlist.append(n)
        main_list.append(randomlist)
        j+=1
    score =  0
    print("Your Score is:", sorting_test(main_list, score),"/ 10")
