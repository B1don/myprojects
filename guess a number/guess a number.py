import random
import math

gamemode = input("Выбери режим: ")
if gamemode == "3":
    guessMade = 1
    rand = random.randint(1, 3)
    while guessMade != 0:
        num = int(input("Введи число: "))
        if num > rand:
            print(f"Моё число меньше {num}")
        elif num < rand:
            print(f"Моё число больше {num}")
        guessMade -= 1
        if num == rand:
            break

    if num == rand:
        print(f"Всё верно! Моё число было: {num}. Ты молодец!")
    else:
        print(f"Ты проиграл, моё число было: {rand}")
if gamemode == "5":
    guessMade = 2
    rand = random.randint(1, 5)
    while guessMade != 0:
        num = int(input("Введи число: "))
        if num > rand:
            print(f"Моё число меньше {num}")
        elif num < rand:
            print(f"Моё число больше {num}")
        guessMade -= 1
        if num == rand:
            break

    if num == rand:
        print(f"Всё верно! Моё число было: {num}. Ты молодец!")
    else:
        print(f"Ты проиграл, моё число было: {rand}")

if gamemode == "10":
    guessMade = 4
    rand = random.randint(1, 10)
    while guessMade != 0:
        num = int(input("Введи число: "))
        if num > rand:
            print(f"Моё число меньше {num}")
        elif num < rand:
            print(f"Моё число больше {num}")
        guessMade -= 1
        if num == rand:
            break

    if num == rand:
        print(f"Всё верно! Моё число было: {num}. Ты молодец!")
    else:
        print(f"Ты проиграл, моё число было: {rand}")


if gamemode == "Свой выбор":
    guessMade = int(input("Количество попыток: "))
    fNumber = int(input("Введи число с начала: "))
    sNumber = int(input("Введи число с конца: "))
    rand = random.randint(fNumber, sNumber)
    while guessMade != 0:
        num = (input("Введи число: ")) # придумать, как проверять вписанное на число и просить выводить число
        num = int(num)
        if num > rand:
            print(f"Моё число меньше {num}")
        elif num < rand:
            print(f"Моё число больше {num}")
        guessMade -= 1
        if num == rand:
            break

    if num == rand:
        print(f"Всё верно! Моё число было: {num}. Ты молодец!")
    else:
        print(f"Ты проиграл, моё число было: {rand}")