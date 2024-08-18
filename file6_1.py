my_people_list = [
    {"name": "Jack", "age": 45},
    {"name": "John", "age": 15},
    {"name": "Bob", "age": 68},
    {"name": "Rob", "age": 25},
    {"name": "Fred", "age": 40},
    {"name": "Arnold", "age": 3},
    {"name": "Alfred", "age": 3},
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
    check_len = len(dict_from_list["name"])
    if check_age < min_age:
        min_age = check_age
    if check_len > name_len:
        name_len = check_len
    sum_age += dict_from_list["age"]
    my_count += 1

for dict_from_list in my_people_list:
    if min_age == dict_from_list["age"]:
        people_age_list.append(dict_from_list["name"])
    if name_len == len(dict_from_list["name"]):
        people_name_list.append(dict_from_list["name"])

print(
    "Імена наймолодших:", people_age_list, "\n"
    "Найдовші імена:", people_name_list, "\n"
    "Середній вік людей:", int(sum_age / my_count),
)
