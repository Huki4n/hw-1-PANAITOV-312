def calculator():
    while(True):
        print("Если хотите выйти в 2 числах напише 0\n")
        # Запрос чисел
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        # Выход из калькулятора
        if num1 == num2 == 0:
            print("\nСпасибо за использование моего калькулятора)))")
            break
        # Запрос действия
        action = str(input("Введите действие(*  /  -  +): "))
        # Функционал калькулятора
        if action == "+":
            print("\nОтвет - ",num1+num2,"\n\n")
        elif action == "-":
            print("\nОтвет - ",num1-num2,"\n\n")
        elif action == "/":
            if num2 != 0:
                print("\nОтвет - ",num1 / num2,"\n\n")
            else:
                print("\nНа ноль делить нельзя","\n\n")
        elif action == "*":
            print("\nОтвет - ",num1*num2,"\n\n")

# Функция вызова
calculator()






