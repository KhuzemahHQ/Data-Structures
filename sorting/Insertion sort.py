# Part1_B: insertionSort

# Time complexity: O(n^2)
def insertion_sort(array):
    # return sorted array
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[j]<array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array


if __name__ == '__main__':
    pass