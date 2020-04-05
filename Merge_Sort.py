# at sololearn another one
def merge_sort(my_list, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(my_list, start, mid)
        merge_sort(my_list, mid, end)
        merge_list(my_list, start, mid, end)
 
def merge_list(my_list, start, mid, end):
    left = my_list[start:mid] #left = my_list[:mid]
    right = my_list[mid:end] #right = my_list[mid:]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            my_list[k] = left[i]
            i = i + 1
        else:
            my_list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            my_list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            my_list[k] = right[j]
            j = j + 1
            k = k + 1
 
 
my_list = input('Enter the list of numbers: ').split()
my_list = [int(x) for x in my_list]
merge_sort(my_list, 0, len(my_list))
print('Sorted list: ', end='')
print(my_list)
