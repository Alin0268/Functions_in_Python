# -*- coding: utf-8 -*-

def binary_search(my_list, key):
    #Search key in my_list[start... end - 1].
    start = 0
    end = len(my_list)
    while start < end:
        mid = (start + end)//2
        if my_list[mid] > key:
            end = mid
        elif my_list[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1

#Вариант без пользовательского ввода в консоли
my_list1 = [2, 4, 6, 7, 9, 23]
key1 = 6
print(binary_search(my_list1, key1))


my_list = input('Enter the sorted list of numbers: ')
my_list = my_list.split()
my_list = [int(x) for x in my_list]
key = int(input('The number to search for: '))
 
index = binary_search(my_list, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
