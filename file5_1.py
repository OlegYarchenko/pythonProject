import keyword
import string

my_reserved_words = keyword.kwlist
all_res_char =string.punctuation
my_res_char_list = []
for my_symb in all_res_char:
    my_res_char_list.append(my_symb)
my_res_char_list.pop(-6)

my_input = input("Введіть ім'я своєї змінної: ")

my_result = ""
my_timer = 0

if my_input in my_reserved_words:
    my_result = "False"
elif my_input.isdigit():
    my_result = "False"
elif my_input.isdigit():
    my_result = "False"
else:
    for my_check_symb in my_input:
        my_timer += 1
        if my_check_symb.isdigit() and my_timer == 1:
            my_result = "False"
        elif my_check_symb in my_res_char_list:
            my_result = "False"
        elif my_check_symb.isupper():
            my_result = "False"
        elif my_check_symb.isspace():
            my_result = "False"
        if my_result == "False":
            break
        else:
            my_result = "True"
print(my_result)
