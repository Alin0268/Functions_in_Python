# -*- coding: utf-8 -*-
def linear_search(mylist, key):
    """Return index of key in mylist. Return -1 if key not present."""
    for i in range(len(mylist)):
        if mylist[i] == key:
            return i
    return -1

# Вариант без пользовательского ввода в консоли
list1 = [2, 4, 5, 89, 23, 22, 1, 4, 98]
print(linear_search(list1, 4))


# Вводим числа через пробел
mylist = input('Enter the list of numbers: ')
mylist = mylist.split()
mylist = [int(x) for x in mylist]
key = int(input('The number to search for: '))
 
index = linear_search(mylist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))


