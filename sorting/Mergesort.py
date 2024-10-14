# Part1_A: Merge Sort


# Time complexity: O(nlogn)
def merge_sort(array):
    if len(array) > 1:
        # dividing the array till arrays have length of 1
        midpoint = int(len(array)/2)
        left = array[:midpoint]
        right = array[midpoint:]
        merge_sort(left)
        merge_sort(right)

        # merging the arrays
        i = 0
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                array[i] = left.pop(0)
            else:
                array[i] = right.pop(0)
            i += 1

        if len(left)>0:
            while len(left) != 0:
                array[i] = left.pop(0)
                i += 1
        if len(right)>0:
            while len(right) != 0:
                array[i] = right.pop(0)
                i += 1

    return array


if __name__ == '__main__':
    pass