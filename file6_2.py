my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}
my_list1 = []
my_list2 = []
my_dict_3 = dict()
my_list_spilne = []
my_dict_4 = dict()

for dict_el in my_dict_1.keys():
    my_list1.append(dict_el)

for dict_el in my_dict_2.keys():
    my_list2.append(dict_el)

my_set1 = set(my_list1)
my_set2 = set(my_list2)

my_union_set = my_set1.union(my_set2)
my_difference_set1 = my_set1.difference(my_set2)
my_difference_set2 = my_set2.difference(my_set1)
my_inter_set = my_set1.intersection(my_set2)


for set_el in my_difference_set1:
    my_dict_3[set_el] = my_dict_1[set_el]

for dict_key, dict_val in my_dict_1.items():
    if dict_key in my_inter_set:
        my_list_spilne.append(dict_val)
    if dict_key in my_difference_set1:
        my_dict_4[dict_key] = dict_val

for dict_key, dict_val in my_dict_2.items():
    if dict_key in my_inter_set:
        my_list_spilne.append(dict_val)
    if dict_key in my_difference_set2:
        my_dict_4[dict_key] = dict_val

my_dict_4[str(my_inter_set)] = my_list_spilne

print(
    "а) список із ключів, які є в обох словниках", my_union_set, "\n"
    "б) список із ключів, які є у першому, але немає у другому словнику", my_difference_set1, "\n"
    "в) словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику", my_dict_3, "\n"
    "г) Об'єднати ці два словники у новий словник за правилом", my_dict_4, "\n"
)
