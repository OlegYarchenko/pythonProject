my_list = [0, 1, 7, 2, 4, 8]
# my_list = [1, 3, 5]
# my_list = [6]
# my_list = []
print(my_list)
if my_list == []:
    print(0)
else:
    my_second_list = my_list[::2]
    print(my_second_list)
    last_list_element = my_list.pop()
    sum_element = 0

    for list_element in my_second_list:
        sum_element += list_element

    print(sum_element * last_list_element)
