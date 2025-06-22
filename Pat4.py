my_list = [1, 2, 3, 4, 5]

if my_list:
    my_list = [my_list[-1]] + my_list[:-1]

print(my_list)
