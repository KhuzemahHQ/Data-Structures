from Part2 import *

def test_insert (heap, ref_vec):
    print("---------------------")
    print("Testing insert_node:")
    print("---------------------")
    
    try:
        counter = 0
        ref_vec_length = len(ref_vec)

        for i in range(ref_vec_length):
            if heap.harr[i].value == ref_vec[i]:
                counter += 1

        score = (counter//ref_vec_length) * 10
        if score == 10:
            print("Test Passed! Score For This Part:", str(score) + "/10")
        else:
            print("Test Failed. Score For This Part:", str(score) + "/10")
    except:
        score = 0
        print("Test Failed. Score For This Part:", str(score) + "/10")
    print()
    return score

def test_delete (heap, ref_vec):
    print("---------------------")
    print("Testing delete_node:")
    print("---------------------")
    
    try:
        counter = 0
        ref_vec_length = len(ref_vec)

        for i in range(ref_vec_length):
    	    if heap.harr[i].value == ref_vec[i]:
    		    counter += 1

        score = (counter//ref_vec_length) * 10
        if score == 10:
            print("Test Passed! Score For This Part:", str(score) + "/10")
        else:
            print("Test Failed. Score For This Part:", str(score) + "/10")
    except:
        score = 0
        print("Test Failed. Score For This Part:", str(score) + "/10")
    print()
    return score

def test_extract_min (heap, ref_vec):
    print("---------------------")
    print("Testing extract_min:")
    print("---------------------")
    
    try:
        counter = 0
        ref_vec.sort()
        ref_vec_length = len(ref_vec)

        for value in ref_vec:
            if heap.extract_min().value == value:
                counter += 1

        score = (counter//ref_vec_length) * 4
        if score == 4:
            print("Test Passed! Score For This Part:", str(score) + "/4")
        else:
            print("Test Failed. Score For This Part:", str(score) + "/4")
    except:
        score = 0
        print("Test Failed. Score For This Part:", str(score) + "/4")
    print()
    return score

def test_decrease_node (heap, ref_vec):
    print("-----------------------")
    print("Testing decrease_node:")
    print("-----------------------")
    
    try:
        counter = 0
        ref_vec_length = len(ref_vec)

        for i in range(ref_vec_length):
    	    if heap.harr[i].value == ref_vec[i]:
    		    counter += 1

        score = (counter//ref_vec_length) * 6
        if score == 6:
            print("Test Passed! Score For This Part:", str(score) + "/6")
        else:
            print("Test Failed. Score For This Part:", str(score) + "/6")
    except:
        score = 0
        print("Test Failed. Score For This Part:", str(score) + "/6")
    print()
    return score

heap = minHeap(40)
ref_vec = []

heap_values = [34,7,53,12,68,90,24,71,13,3,1,61,18,30,50,11,52,54,56,55,80,97,91,23,29,33,73,77,89,16,20,35,43,47,57,66,88,2,9,64]
vector_values = [1,2,16,3,7,23,18,13,9,55,12,24,33,53,20,35,47,54,11,64,80,97,91,90,29,61,73,77,89,50,30,71,43,52,57,66,88,56,34,68]



print("Starting Tests")
print()

score = 0


# Testing Insertion
try:
    for i in range(40):
        heap.insert_node(heap_values[i])
        ref_vec.append(vector_values[i])
    score += test_insert(heap, ref_vec)
except:
    score += 0

del_indices = [5,11,17,29,33,21,34,5,9]
try:
    for i in del_indices:
        heap.delete_node(i)

    remaining_values = [1,2,16,3,7,33,18,13,9,43,12,34,61,53,20,35,47,56,11,64,80,57,91,90,68,66,73,77,89,88,30,71]
    ref_vec.clear()
    for value in remaining_values:
        ref_vec.append(value)

    # Testing Delete
    score += test_delete(heap, ref_vec)
except:
    score += 0

# Testing extract_min
try:
    score += test_extract_min(heap, ref_vec)
except:
    score += 0

# Testing decrease_node
try:
    heap = minHeap(12)
    final_values = [121, 51, 111, 31, 101, 21, 91, 41, 81, 11, 71, 61]
    decreased_values = [2, 19, 11, 20, 41, 31, 91, 121, 21, 101, 71, 111]
    ref_vec.clear()

    for i in range(12):
        heap.insert_node(final_values[i])
        ref_vec.append(decreased_values[i])


    heap.decrease_node(3, 20)
    heap.decrease_node(8, 19)
    heap.decrease_node(5, 2)


    score += test_decrease_node(heap, ref_vec)
except:
    score += 0
    print("----------------------")
    print("Testing decrease_node:")
    print("----------------------")
    print("Test Failed. Score For This Part:", str(score) + "/6")
    print()

print("Total Score:", str(score)+"/30")
