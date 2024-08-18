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
name_len = 0
people_name_list = []
sum_age = 0
my_count = 0

for dict_from_list in my_people_list:
    check_age = dict_from_list["age"]
    if check_age < min_age:
        min_age = check_age

for dict_from_list in my_people_list:
    if min_age == dict_from_list["age"]:
        people_age_list.append(dict_from_list["name"])

for dict_from_list in my_people_list:
    check_len = len(dict_from_list["name"])
    if check_len > name_len:
        name_len = check_len

for dict_from_list in my_people_list:
    if name_len == len(dict_from_list["name"]):
        people_name_list.append(dict_from_list["name"])

for dict_from_list in my_people_list:
    sum_age += dict_from_list["age"]
    my_count += 1

print(
    "Імена наймолодших:", people_age_list, "\n"
    "Найдовші імена:", people_name_list, "\n"
    "Середній вік людей", int(sum_age / my_count),
)
