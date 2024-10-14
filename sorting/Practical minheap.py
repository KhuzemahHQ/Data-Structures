from Part2 import *
from Part1_A import merge_sort
from Part1_B import insertion_sort

# return list of printing job strings
def job_string_maker (printing_jobs):
    final_list = []
    for job in printing_jobs:
        time = job[3]
        hour = time[:2]
        minute = time[-2:]
        page = str(job[0])
        doc = job[1]
        string = hour+minute+page+doc
        final_list.append(string)
    return final_list

# return list of sorted printing jobs
# mention the reason for choosing a particular sorting algorithm here -----?

# I will be using mergesort as it has a better time complexity of O(nlogn) compared to insertionssort with O(n^2)
def job_string_sorter (job_strings):
    job_strings = merge_sort(job_strings)
    return job_strings

# return list of printing jobs with assigned properties
def assign_priorities (sorted_job_strings, printing_jobs):
    for string in sorted_job_strings:
        for job in printing_jobs:
            if job_string_maker([job])[0] == string:
                job[2] = sorted_job_strings.index(string) + 1
    return printing_jobs

# return list of document names in correct printing order    
def create_heap(prioritized_printing_jobs):
    heap = minHeap(len(prioritized_printing_jobs))
    for job in prioritized_printing_jobs:
        heap.insert_node(job[2],job[1])
    title_list = []
    while heap.heap_size > 0:
        next = heap.extract_min()
        title_list.append(next.doc_title)
    # print(title_list)
    return title_list

# if __name__ == '__main__':
#     driver program