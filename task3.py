# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1000)
count = 10
entered_number = float(input("Введите число: "))
while entered_number != num and count > 1:
    count -= 1
    if entered_number > num:
        print("Введите число меньше")
        print("Осталось вот столько попыток:", count)
    elif entered_number < num:
        print("Введите число больше")
        print("Осталось вот столько попыток:", count)
    entered_number = float(input("Повтори попытку: "))
print ("Это было число", num)
if entered_number == num:
    print("Вы угадали!")