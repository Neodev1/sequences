# #модуль3
# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
# Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
# Введите элементы 2-го списка: 2,5
# Результат: 1,3,4

numbers = str(input('Введите числа через запятую:'))
first_numbers = numbers.split(',')
numbers = str(input('Введите числа через запятую:'))
second_numbers = numbers.split(',')
for number in first_numbers[:]:
    if number in second_numbers:
        first_numbers.remove(number)
print(first_numbers)
