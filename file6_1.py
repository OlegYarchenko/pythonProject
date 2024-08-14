my_people_list = [
    {"name": "Jack", "age": 45},
    {"name": "John", "age": 15},
    {"name": "Bob", "age": 68},
    {"name": "Rob", "age": 25},
    {"name": "Fred", "age": 40},
    {"name": "Tom", "age": 33},
    {"name": "Den", "age": 15},
]

people_age_list = []
min_age = 1000
list_age = []


for dict_from_list in my_people_list:
    # print(dict_from_list.items())
    check_age = dict_from_list["age"]
    # print('1', check_age)
    if check_age < min_age:
        min_age = check_age
        # print('2', min_age)
        # if min_age == dict_from_list["age"]:
        #     people_age_list.append(dict_from_list)

for dict_from_list in my_people_list:
    if min_age == dict_from_list["age"]:
        people_age_list.append(dict_from_list)

# for dict_from_list in my_people_list:
#     # print(dict_from_list.items())
#     check_age = dict_from_list["age"]
#     if check_age not in list_age:
#         list_age.append(check_age)
#
# for _ in list_age:
#     if _ < min_age:
#         min_age = _
#         print(min_age)

# print("низ", min_age)
# set_age = set(list_age)
print(people_age_list)
