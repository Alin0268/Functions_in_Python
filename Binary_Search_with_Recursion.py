# -*- coding: utf-8 -*-

def binary_search(my_list, from_my, to_my, key):
    #Search key in my_list[...from_my...to_my...end - 1].
    if to_my >= from_my:
        mid = from_my + (to_my - from_my)//2
        if my_list[mid] == key:
            return mid
        elif my_list[mid] > key:
            return binary_search(my_list, from_my, mid-1, key)
        else:
            return binary_search(my_list, mid+1, to_my, key)
    else:
        return -1

 
my_list = input('Enter the sorted list of numbers: ')
my_list = my_list.split()
my_list = [int(x) for x in my_list]
key = int(input('The number to search for: '))
 
index = binary_search(my_list, 0, len(my_list)-1, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))


#Вариант без пользовательского ввода в консоли
my_list1 = [2, 4, 6, 7, 9, 23]
key1 = 6
print(binary_search(my_list1, 0, len(my_list)-1, key1))
