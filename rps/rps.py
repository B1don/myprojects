import random
import time

possible_actions = ["камень", "бумага", "ножницы"]
i = 3
userPoint = 0
pcPoint = 0

amountPoint = int(input("До скольки очков играем: "))

while userPoint or pcPoint <= amountPoint:
    user_action = input("Твой выбор: ")
    time.sleep(1)

    while i > 0:
        print(f"{i}...")
        i -= 1
        time.sleep(1)
    i = 3
    pc_action = random.choice(possible_actions)

    if user_action == pc_action:
        print(f"Ничья! И пользователь, и компьютер выбрали {pc_action}.")
    elif user_action == "камень":
        if pc_action == "ножницы":
            print("Я выбрал ножницы! Ты победил этот круг!")
            userPoint += 1
        else:
            print("Я выбрал бумагу! Ты проиграл этот круг.")
            pcPoint += 1
    elif user_action == "бумага":
        if pc_action == "камень":
            print("Я выбрал камень! Ты победил этот круг!")
            userPoint += 1
        else:
            print("Я выбрал ножницы! Ты проиграл этот круг.")
            pcPoint += 1
    elif user_action == "ножницы":
        if pc_action == "бумага":
            print("Я выбрал бумагу! Ты победил этот круг!")
            userPoint += 1
        else:
            print("Я выбрал камень! Ты проиграл этот круг.")
            pcPoint += 1
    print(f"Твои очки: {userPoint} \t Очки компьютера: {pcPoint}")
    if userPoint == amountPoint:
        print("Ты дошёл до назначенного количества очков! Ты выиграл игру!")
        break
    if pcPoint == amountPoint:
        print("Я дошёл до назначенного количества очков! Я выиграл игру!")
        break   