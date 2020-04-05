def select(my_list, start, end, i):
    """Find ith smallest element in my_list[start... end-1]."""
    if end - start <= 1:
        return my_list[start]
    pivot = partition(my_list, start, end)
 
    # number of elements in my_list[start... pivot]
    k = pivot - start + 1
 
    if i < k:
        return select(my_list, start, pivot, i)
    elif i > k:
        return select(my_list, pivot + 1, end, i - k)
 
    return my_list[pivot]
 
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
 
 
my_list = input('Enter the list of numbers: ')
my_list = my_list.split()
my_list = [int(x) for x in my_list]
i = int(input('The ith smallest element will be found. Enter i: '))
 
ith_smallest_item = select(my_list, 0, len(my_list), i)
print('Result: {}.'.format(ith_smallest_item))
