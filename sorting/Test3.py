from Part2 import *
from Part3 import *


number_of_jobs = 50

job_1 = [8, "D", -1, "11:30"]
job_2 = [2, "B", -1, "19:15"]
job_3 = [8, "A", -1, "21:50"]
job_4 = [8, "F", -1, "09:20"]
job_5 = [8, "M", -1, "04:20"]
job_6 = [5, "E", -1, "09:30"]
job_7 = [8, "C", -1, "23:59"]
job_8 = [8, "G", -1, "00:00"]
job_9 = [8, "H", -1, "01:30"]
job_10 = [8, "I", -1, "11:22"]
job_11 = [8, "D", -1, "19:27"]
job_12 = [2, "B", -1, "21:19"]
job_13 = [8, "A", -1, "15:18"]
job_14 = [8, "F", -1, "17:02"]
job_15 = [8, "M", -1, "07:20"]
job_16 = [5, "E", -1, "19:00"]
job_17 = [8, "C", -1, "01:14"]
job_18 = [8, "G", -1, "21:31"]
job_19 = [8, "H", -1, "17:22"]
job_20 = [8, "I", -1, "16:47"]
job_21 = [8, "M", -1, "22:30"]
job_22 = [2, "B", -1, "21:15"]
job_23 = [8, "A", -1, "10:00"]
job_24 = [8, "F", -1, "21:00"]
job_25 = [8, "M", -1, "14:50"]
job_26 = [5, "E", -1, "16:05"]
job_27 = [8, "C", -1, "17:55"]
job_28 = [8, "G", -1, "12:30"]
job_29 = [8, "H", -1, "11:40"]
job_30 = [8, "I", -1, "09:15"]
job_31 = [8, "M", -1, "01:15"]
job_32 = [2, "B", -1, "01:45"]
job_33 = [8, "A", -1, "20:05"]
job_34 = [8, "F", -1, "18:50"]
job_35 = [8, "M", -1, "17:40"]
job_36 = [5, "E", -1, "16:20"]
job_37 = [8, "C", -1, "15:30"]
job_38 = [8, "G", -1, "17:10"]
job_39 = [8, "H", -1, "18:40"]
job_40 = [8, "I", -1, "19:10"]
job_41 = [8, "M", -1, "10:25"]
job_42 = [2, "B", -1, "22:25"]
job_43 = [8, "A", -1, "23:25"]
job_44 = [8, "F", -1, "23:59"]
job_45 = [8, "M", -1, "22:53"]
job_46 = [5, "E", -1, "16:53"]
job_47 = [8, "C", -1, "17:43"]
job_48 = [8, "G", -1, "13:20"]
job_49 = [8, "H", -1, "13:40"]
job_50 = [8, "I", -1, "14:40"]

printing_jobs = [
    job_1, job_2, job_3, job_4, job_5, job_6, job_7, job_8, job_9, job_10,
    job_11, job_12, job_13, job_14, job_15, job_16, job_17, job_18, job_19, job_20,
    job_21, job_22, job_23, job_24, job_25, job_26, job_27, job_28, job_29, job_30,
    job_31, job_32, job_33, job_34, job_35, job_36, job_37, job_38, job_39, job_40,
    job_41, job_42, job_43, job_44, job_45, job_46, job_47, job_48, job_49, job_50
                ]

print("Running Tests for Part 3:")
print()

total_score = 0

print("--------------------------------------------")
print("Testing String Sequences for Printing Jobs:")
print("--------------------------------------------")
try:
    test_fail = False
    job_strings = job_string_maker (printing_jobs)
    test_job_strings = ['11308D', '19152B', '21508A', '09208F', '04208M', '09305E', '23598C', '00008G', '01308H', '11228I', '19278D', '21192B', '15188A', '17028F', '07208M', '19005E', '01148C', '21318G', '17228H', '16478I', '22308M', '21152B', '10008A', '21008F', '14508M', '16055E', '17558C', '12308G', '11408H', '09158I', '01158M', '01452B', '20058A', '18508F', '17408M', '16205E', '15308C', '17108G', '18408H', '19108I', '10258M', '22252B', '23258A', '23598F', '22538M', '16535E', '17438C', '13208G', '13408H', '14408I']
    for i in range(number_of_jobs):
        if job_strings[i] != test_job_strings[i]:
            test_fail = True
            break
    if test_fail == True:
        total_score += 0
        print("Test Failed. Total Score:", str(total_score), "/40")
        print()
    else:
        total_score += 10
        print("Test Passed! Total Score:", str(total_score), "/40")
        print()
except:
    print("Test Failed. Total Score:", str(total_score), "/40")
    print()

print("---------------------------------------------------")
print("Testing String Sequences for Sorted Printing Jobs:")
print("---------------------------------------------------")
try:
    test_fail = False
    sorted_job_strings = job_string_sorter(job_strings)
    test_sorted_job_strings = ['00008G', '01148C', '01158M', '01308H', '01452B', '04208M', '07208M', '09158I', '09208F', '09305E', '10008A', '10258M', '11228I', '11308D', '11408H', '12308G', '13208G', '13408H', '14408I', '14508M', '15188A', '15308C', '16055E', '16205E', '16478I', '16535E', '17028F', '17108G', '17228H', '17408M', '17438C', '17558C', '18408H', '18508F', '19005E', '19108I', '19152B', '19278D', '20058A', '21008F', '21152B', '21192B', '21318G', '21508A', '22252B', '22308M', '22538M', '23258A', '23598C', '23598F']
    for i in range(number_of_jobs):
        if sorted_job_strings[i] != test_sorted_job_strings[i]:
            test_fail = True
            break
    if test_fail == True:
        total_score += 0
        print("Test Failed. Total Score:", str(total_score), "/40")
        print()
    else:
        total_score += 5
        print("Test Passed! Total Score:", str(total_score), "/40")
        print()
    
except:
    print("Test Failed. Total Score:", str(total_score), "/40")
    print()

print("----------------------------")
print("Testing Assigned Priorities:")
print("----------------------------")
try:
    test_fail = False
    prioritized_printing_jobs = assign_priorities(sorted_job_strings, printing_jobs)
    test_assigned_priorities = [ 14,37,44,9,6,10,49,1,4,13,38,42,21,27,7,35,2,43,29,25,46,41,11,40,20,23,32,16,15,8,3,5,39,34,30,24,22,28,33,36,12,45,48,50,47,26,31,17,18,19 ]

    for i in range(number_of_jobs):
        if prioritized_printing_jobs[i][2] != test_assigned_priorities[i]:
            test_fail = True
            break
    if test_fail == True:
        total_score += 0
        print("Test Failed. Total Score:", str(total_score), "/40")
        print()
    else:
        total_score += 10
        print("Test Passed! Total Score:", str(total_score), "/40")
        print()
    
except:
    print("Test Failed. Total Score:", str(total_score), "/40")
    print()

try:
    min_heap = minHeap(number_of_jobs)
    for i in range(number_of_jobs):
        min_heap.insert_node(prioritized_printing_jobs[i][2], prioritized_printing_jobs[i][1])
except:
    print("------------------------------")
    print("Can't insert into the heap :/")
    print("------------------------------")
    print()

print("----------------------------------")
print("Testing Final Print Job Sequence:")
print("----------------------------------")
try:
    test_fail = False
    prioritized_document_names = []
    test_prioritized_document_names = ['G', 'C', 'M', 'H', 'B', 'M', 'M', 'I', 'F', 'E', 'A', 'M', 'I', 'D', 'H', 'G', 'G', 'H', 'I', 'M', 'A', 'C', 'E', 'E', 'I', 'E', 'F', 'G', 'H', 'M', 'C', 'C', 'H', 'F', 'E', 'I', 'B', 'D', 'A', 'F', 'B', 'B', 'G', 'A', 'B', 'M', 'M', 'A', 'C', 'F']
    for i in range(number_of_jobs):
        document = min_heap.extract_min()
        prioritized_document_names.append(document.doc_title)

    for i in range(number_of_jobs):
        if prioritized_document_names[i] != test_prioritized_document_names[i]:
            test_fail = True
            break
    if test_fail == True:
        total_score += 0
        print("Test Failed. Total Score:", str(total_score), "/40")
        print()
    else:
        total_score += 15
        print("Test Passed! Total Score:", str(total_score), "/40")
        print()
   
except:
    print("Test Failed. Total Score:", str(total_score), "/40")
    print()


