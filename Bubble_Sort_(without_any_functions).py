 
my_list = input('Enter the list of numbers: ').split()
my_list = [int(x) for x in my_list]

for i in range(len(my_list) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if my_list[j + 1] < my_list[j]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                no_swap = False
        if no_swap:
            continue
print('Sorted list: ', end='')
print(my_list)
