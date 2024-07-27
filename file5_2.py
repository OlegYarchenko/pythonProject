while True:
    my_status_program = input("Запустити калькулятор? (y/n): " )
    if my_status_program == "y":
        input_chislo1 = input("Введіть перше число: ")
        input_chislo2 = input("Введіть друге число: ")
        input_dija = input("Яку дію слід виконати (+,-,*,/)?: ")
        if input_dija == "+":
            print(int(input_chislo1) + int(input_chislo2))
        elif input_dija == "-":
            print(int(input_chislo1) - int(input_chislo2))
        elif input_dija == "*":
            print(int(input_chislo1) * int(input_chislo2))
        elif input_dija == "/":
            if int(input_chislo2) == 0:
                print("На нуль ділити не можна!")
            else:
                print(int(input_chislo1) / int(input_chislo2))
        else:
            print("Ви щось не те ввели(")
    elif my_status_program == "n":
        break
    else:
        print("Ви щось не так ввели")
