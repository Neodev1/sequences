#Модуль 2

number=str(input('Введите числа через запятую:'))
numbers=number.split(',')
result=[]
for figure in numbers:
    if numbers.count(figure) == 1:
        result.append(figure)
print(result)
