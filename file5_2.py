my_dija_list = ["+", "-", "*", "/"]

while True:
    my_status_program = input("Запустити калькулятор? (y/n): " )
    if my_status_program == "y":
        input_chislo1 = input("Введіть перше число: ")
        input_chislo2 = input("Введіть друге число: ")
        input_dija = input("Яку дію слід виконати (+,-,*,/)?: ")
        if input_dija == "+" and input_chislo1.isdigit() and input_chislo2.isdigit() and input_dija in my_dija_list:
            my_result = int(input_chislo1) + int(input_chislo2)
        elif input_dija == "-" and input_chislo1.isdigit() and input_chislo2.isdigit() and input_dija in my_dija_list:
            my_result = int(input_chislo1) - int(input_chislo2)
        elif input_dija == "*" and input_chislo1.isdigit() and input_chislo2.isdigit() and input_dija in my_dija_list:
            my_result = int(input_chislo1) * int(input_chislo2)
        elif input_dija == "/" and input_chislo1.isdigit() and input_chislo2.isdigit() and input_dija in my_dija_list:
            if int(input_chislo2) == 0:
                my_result = "На нуль ділити не можна!"
            else:
                my_result = int(input_chislo1) / int(input_chislo2)
        else:
            my_result = "Ви щось не те ввели("
    elif my_status_program == "n":
        break
    else:
        my_result = "Ви щось не так ввели"
    print(my_result)
