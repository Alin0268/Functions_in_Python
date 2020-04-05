# -*- coding: utf-8 -*-

def heapsort(my_list):
    build_max_heap(my_list)
    for i in range(len(my_list) - 1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        max_heapify(my_list, index=0, size=i)
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(my_list):
    length = len(my_list)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(my_list, index=start, size=length)
        start = start - 1
 
def max_heapify(my_list, index, size):
    l = left(index)
    r = right(index)
    if (l < size and my_list[l] > my_list[index]):
        largest = l
    else:
        largest = index
    if (r < size and my_list[r] > my_list[largest]):
        largest = r
    if (largest != index):
        my_list[largest], my_list[index] = my_list[index], my_list[largest]
        max_heapify(my_list, largest, size)
 
 
my_list = input('Enter the list of numbers: ').split()
my_list = [int(x) for x in my_list]
heapsort(my_list)
print('Sorted list: ', end='')
print(my_list)