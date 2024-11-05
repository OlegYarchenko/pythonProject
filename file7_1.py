def say_hi(name, age):
    my_str = "Hi. My name is my_name and I'm my_age years old"
    change_name= my_str.replace("my_name", name)
    change_age = change_name.replace("my_age", str(age))
    result = change_age

    return result


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
