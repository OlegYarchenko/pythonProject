my_list = [0, 1, 0, 12, 3]
# my_list = [0]
# my_list = [1, 0, 13, 0, 0, 0, 5]
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(my_list)
list_len = len(my_list)

for list_index in my_list:
    if list_index == 0:
        my_list.insert(list_len, my_list.pop(my_list.index(list_index)))

print(my_list)
