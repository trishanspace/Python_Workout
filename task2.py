import fractions

# 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

numA_1, numA_2 = map(int, input("Введите дробь с числителем и знаменателем 1: ").split("/"))
numB_1, numB_2 = map(int, input("Введите дробь с числителем и знаменателем 2: ").split("/"))

pair_numbers1 = fractions.Fraction(numA_1, numA_2)
pair_numbers2 = fractions.Fraction(numB_1, numB_2)

res = (numA_1 * numB_2 + numA_2 * numB_1) / (numA_2 * numB_2)
print (f"{res}, {pair_numbers1 + pair_numbers2}")

res = (numA_1 * numB_1) / (numA_2 * numB_2)
print (f"{res}, {pair_numbers1 * pair_numbers2}")