#модуль 1
count=int(input('Введите количество элэментов:'))
result=[]
for i in range(count):
    figure=int(input('Введите цифру:'))
    result.append(figure)
result.sort()
print(result)