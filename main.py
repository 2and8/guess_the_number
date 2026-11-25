
import random

print("=" * 22)
print("-----Угадай число-----")
print("=" * 22)

a = random.randint(1, 100)
pop = 0

while True:
    try:
        b = int(input("Какое число мы загадали? (1-100): "))
        
        if b < 1 or b > 100:
            print("Введите число от 1 до 100!")
            continue

        pop += 1

        if a > b:
            print("Наше число больше")

        elif a < b:
            print("Наше число меньше")

        else:
            print("Вы угадали!!!")

            if pop % 10 == 1 and pop % 100 != 11:
                print(f"Вы угадали за {pop} попытку")
            elif pop % 10 in (2, 3, 4) and pop % 100 not in (12, 13, 14):
                print(f"Вы угадали за {pop} попытки")
            else:
                print(f"Вы угадали за {pop} попыток")

            break

    except ValueError:
        print("Введите число, а не буквы!")
