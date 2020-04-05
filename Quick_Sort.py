# -*- coding: utf-8 -*-

#at sololearn another one
def quicksort(my_list, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(my_list, start, end)
        quicksort(my_list, start, p)
        quicksort(my_list, p + 1, end)
 
 
def partition(my_list, start, end):
    pivot = my_list[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and my_list[i] <= pivot):
            i = i + 1
        while (i <= j and my_list[j] >= pivot):
            j = j - 1
 
        if i <= j:
            my_list[i], my_list[j] = my_list[j], my_list[i]
        else:
            my_list[start], my_list[j] = my_list[j], my_list[start]
            return j
 
#Вариант без пользовательского вывода
list1 = [2, 4, 65, 32, 85, 1, 98, 324]
quicksort(list1, 0, len(list1)-1)
print(list1)

 
my_list = input('Enter the list of numbers: ').split()
my_list = [int(x) for x in my_list]
quicksort(my_list, 0, len(my_list))
print('Sorted list: ', end='')
print(my_list)
