# -*- coding: utf-8 -*-
"""Return index of key in mylist. Return -1 if key not present."""

# Вводим числа через пробел
mylist = input('Enter the list of numbers: ')
mylist = mylist.split()
mylist = [int(x) for x in mylist]
key = int(input('The number to search for: '))

indicator = 0
for i in range(len(mylist)):
    if mylist[i] == key:
        print('first occurrence of {} was found at index {}.'.format(key, i))
        indicator = 1
        break
if indicator == 0:
    print('{} was not found.'.format(key))
    

