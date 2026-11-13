print("ФИНАНСОВЫЙ КАЛЬКУЛЯТОР")

n = 1

while n != 0:

    print("\nВыберите операцию:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")
    print("5 - Возведение в степень")
    print("6 - Остаток от деления")
    print("7 - Целочисленное деление")
    print("8 - Расчёт скидки")
    print("9 - Расчёт прибыли")
    print("10 - Расчёт наценки")
    print("0 - Выход")

    n = int(input("Введите номер операции: "))

    if n == 0:
        print("Программа завершена")

    elif n >= 1 and n <= 7:

        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))

        if n == 1:
            c = a + b

        elif n == 2:
            c = a - b

        elif n == 3:
            c = a * b

        elif n == 4:
            if b != 0:
                c = a / b
            else:
                print("На ноль делить нельзя!")
                c = None

        elif n == 5:
            c = a ** b

        elif n == 6:
            if b != 0:
                c = a % b
            else:
                print("На ноль делить нельзя!")
                c = None

        elif n == 7:
            if b != 0:
                c = a // b
            else:
                print("На ноль делить нельзя!")
                c = None

        if c != None:
            print("Ответ:", c)

    elif n == 8:
        a = int(input("Введите стоимость товара: "))
        b = int(input("Введите скидку в процентах: "))
        c = a - (a * b / 100)
        print("Цена со скидкой:", c)

    elif n == 9:
        a =int(input("Введите доход: "))
        b = int(input("Введите расходы: "))
        c = a - b
        print("Ваша прибыль:",c)

    elif n == 10:
        a = int(input("Введите стоимость товара: "))
        b = int(input("Введите наценку в процентах: "))
        c = a + (a * b / 100)
        print("Цена с наценкой:", c)

    else:
        print("Неверный номер операции!")

print("До свидания!")