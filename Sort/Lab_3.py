import pickle
import json
from tqdm import tqdm


def read_data(path: str) -> list:
    with open(path, 'r') as read_from:
        data = json.load(read_from)
        return data


'''def insertion_sort(list1):
    # Outer loop to traverse through 1 to len(list1)
    with tqdm(list1, desc='Сортиртировка',  colour="#FFFFFF") as progressbar:
        for i in range(1, len(list1)):
            j = i
            while j >= 0:# and int(list1[j - 1]['age']) > int(list1[j]['age']):
                #list1[j - 1], list1[j] = list1[j], list1[j - 1]
                #j -= 1
                heapsort(list1)
            progressbar.update(1)
        progressbar.update(1)
    return list1'''



def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)


def parent(i) -> int:
    return (i - 1) // 2


def left(i) -> int:
    return 2 * i + 1


def right(i) -> int:
    return 2 * i + 2


def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1


def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and int(alist[l]['weight']) > int(alist[index]['weight'])):
        largest = l
    else:
        largest = index
    if (r < size and int(alist[r]['weight']) > int(alist[largest]['weight'])):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)

'''
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
heapsort(alist)
print('Sorted list: ', end='')
print(alist)

file_to_read = input()
with open(file_to_read, "r") as data:
    data = pickle.load(data['weight'])

heapsort(data)
with open("D:\\for_lab_3.txt", "r") as res:
    res = pickle.dumps(data)
'''

'''#with open("D:\\for_lab_3.txt", "r") as f:
data_to_sort = read_data("D:\\for_lab_3_1.txt")
heapsort(data_to_sort)
with open("D:\\axyet.txt", "w") as output_file:
    json.dump(data_to_sort, output_file, ensure_ascii=False, indent=1)
print("Ready!")'''
