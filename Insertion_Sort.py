def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (j >= 0 and temp < my_list[j]):
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j + 1] = temp
 
 
my_list = input('Enter the list of numbers: ').split()
my_list = [int(x) for x in my_list]
insertion_sort(my_list)
print('Sorted list: ', end='')
print(my_list)