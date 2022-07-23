# модуль4

days={
    '01':'первое',
    '02':'второе',
    '03':'третье',
    '04':'четвертое',
    '05':'пятое',
    '06':'шестое',
    '07':'седьмое',
    '08':'восьмое',
    '09':'девятое',
    '10':'десятое',
    '11':'одиннадцатое',
    '12':'двеннадцатое',
    '13':'триннадцатое',
    '14':'четырнадцатое',
    '15':'пятнадцатое',
    '16':'шестнадцатое',
    '17':'семнадцатое',
    '18':'восемнадцатое',
    '19':'девятнадцатое',
    '20':'двадцатое',
    '21':'двадцать первое',
    '22':'двадцать второе',
    '23':'двадцать третье',
    '24':'двадцать четвертое',
    '25':'двадцать пятое',
    '26':'двадцать шестое',
    '27':'двадцать седьмое',
    '28':'двадцать восьмое',
    '29':'двадцать девятое',
    '30':'тридцатое',
    '31':'тридцать первое'
}
months={
    '01':'января',
    '02':'февраля',
    '03':'марта',
    '04':'апреля',
    '05':'мая',
    '06':'июня',
    '07':'июля',
    '08':'августа',
    '09':'сентября',
    '10':'октября',
    '11':'ноября',
    '12':'декабря'
}
print('Викторина  начинается!')
import random
bornyears=['bornyear1', 'bornyear2', 'bornyear3', 'bornyear4', 'bornyear5', 'bornyear6', 'bornyear7']
result=random.sample(bornyears, 5)
print(result)
total = 0
for bornyear in result:
    if bornyear == 'bornyear1':
        bornyear1 = (input('Введите дату рождения А.С.Пушкина в формате dd.mm.yy: '))
        if bornyear1 == '06.06.1799':
            total += 1
        else:
            data='06.06.1799'
            day, month, year = data.split('.')
            print(days[day], months[month], year, 'года')
    if bornyear == 'bornyear2':
        bornyear2 = (input('Введите дату рождения Д.И.Менделеева в формате dd.mm.yy: '))
        if bornyear2 == '08.02.1834':
            total += 1
        else:
            data='08.02.1834'
            day, month, year = data.split('.')
            print(days[day], months[month], year, 'года')
    if bornyear == 'bornyear3':
        bornyear3 = (input('Введите дату рождения Леонардо Да Винчи в формате dd.mm.yy: '))
        if bornyear3 == '15.04.1452':
            total += 1
        else:
            data='15.04.1452'
            day, month, year = data.split('.')
            print(days[day], months[month], year, 'года')
    if bornyear == 'bornyear4':
        bornyear4 = (input('Введите дату рождения Адриано Челентано в формате dd.mm.yy: '))
        if bornyear4 == '06.01.1938':
            total += 1
        else:
            data='06.01.1938'
            day, month, year = data.split('.')
            print(days[day], months[month], year, 'года')
    if bornyear == 'bornyear5':
        bornyear5 = (input('Введите дату рождения Джим Кэрри в формате dd.mm.yy: '))
        if bornyear5 == '17.01.1962':
            total += 1
        else:
            data = '17.01.1962'
            day, month, year = data.split('.')
            print(days[day], months[month], year, 'года')
    if bornyear == 'bornyear6':
        bornyear6 = (input('Введите дату рождения Джекки Чан в формате dd.mm.yy: '))
        if bornyear6 == '07.04.1954':
            total += 1
        else:
            data='07.04.1954'
            day, month, year = data.split('.')
            print(days[day], months[month], year, 'года')
    if bornyear == 'bornyear7':
        bornyear7 = (input('Введите дату рождения Киану Ривз в формате dd.mm.yy: '))
        if bornyear7 == '02.09.1964':
            total += 1
        else:
            data='02.09.1964'
            day, month, year = data.split('.')
            print(days[day], months[month], year, 'года')
print('Количество правильных ответов: ', total)
print('Количество ошибок: ', 5 - total)
print('Процент правильных ответов: ', (total * 100) / 5)
print('Процент неправильных ответов: ', (5 - total) * 100 / 5)
print('Хотите начать игру сначала?')
otvet = input()
while otvet == 'да':
    print('Викторина  начинается!')
    import random
    bornyears = ['bornyear1', 'bornyear2', 'bornyear3', 'bornyear4', 'bornyear5', 'bornyear6', 'bornyear7']
    result = random.sample(bornyears, 5)

    total = 0
    for bornyear in result:
        if bornyear == 'bornyear1':
            bornyear1 = (input('Введите дату рождения А.С.Пушкина в формате dd.mm.yy: '))
            if bornyear1 == '06.06.1799':
                total += 1
            else:
                data = '06.06.1799'
                day, month, year = data.split('.')
                print(days[day], months[month], year, 'года')
        if bornyear == 'bornyear2':
            bornyear2 = (input('Введите дату рождения Д.И.Менделеева в формате dd.mm.yy: '))
            if bornyear2 == '08.02.1834':
                total += 1
            else:
                data = '08.02.1834'
                day, month, year = data.split('.')
                print(days[day], months[month], year, 'года')
        if bornyear == 'bornyear3':
            bornyear3 = (input('Введите дату рождения Леонардо Да Винчи в формате dd.mm.yy: '))
            if bornyear3 == '15.04.1452':
                total += 1
            else:
                data = '15.04.1452'
                day, month, year = data.split('.')
                print(days[day], months[month], year, 'года')
        if bornyear == 'bornyear4':
            bornyear4 = (input('Введите дату рождения Адриано Челентано в формате dd.mm.yy: '))
            if bornyear4 == '06.01.1938':
                total += 1
            else:
                data = '06.01.1938'
                day, month, year = data.split('.')
                print(days[day], months[month], year, 'года')
        if bornyear == 'bornyear5':
            bornyear5 = (input('Введите дату рождения Джим Кэрри в формате dd.mm.yy: '))
            if bornyear5 == '17.01.1962':
                total += 1
            else:
                data = '17.01.1962'
                day, month, year = data.split('.')
                print(days[day], months[month], year, 'года')
        if bornyear == 'bornyear6':
            bornyear6 = (input('Введите дату рождения Джекки Чан в формате dd.mm.yy: '))
            if bornyear6 == '07.04.1954':
                total += 1
            else:
                data = '07.04.1954'
                day, month, year = data.split('.')
                print(days[day], months[month], year, 'года')
        if bornyear == 'bornyear7':
            bornyear7 = (input('Введите дату рождения Киану Ривз в формате dd.mm.yy: '))
            if bornyear7 == '02.09.1964':
                total += 1
            else:
                data = '02.09.1964'
                day, month, year = data.split('.')
                print(days[day], months[month], year, 'года')
    print('Количество правильных ответов: ', total)
    print('Количество ошибок: ', 5 - total)
    print('Процент правильных ответов: ', (total * 100) / 5)
    print('Процент неправильных ответов: ', (5 - total) * 100 / 5)
    print('Хотите начать игру сначала?')
    otvet = input()