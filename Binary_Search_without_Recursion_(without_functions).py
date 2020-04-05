# -*- coding: utf-8 -*-

my_list = input('Enter the sorted list of numbers: ')
my_list = my_list.split()
my_list = [int(x) for x in my_list]
key = int(input('The number to search for: '))


indicator = False

start = 0
end = len(my_list)
while start < end:
    mid = (start + end)//2
    if my_list[mid] > key:
        end = mid
    elif my_list[mid] < key:
        start = mid + 1
    else:
        print('{} was found at index {}.'.format(key, mid))
        indicator = True
        break
if not(indicator):
    print('{} was not found.'.format(key))
    
