import copy
# Lesson_05
# Практическое задание № 1
print('Практическое задание № 1')
# Удалите из первого списка ВСЕ элементы присутствующие во втором списке.
# 1 способ (ошибочный)
# при приведении ко множеству удаляются дубликаты в списках
list_a = [2, 2, 8, 5, 12, 12, 12, 4, 4]
list_b = [2, 7, 3, 12]
result_list = set(list_a) - set(list_b)
print(list(result_list))
# 1 способ (ошибочный)
# после прохождения циклом первого списка из него удаляются дубли, но сам первый список при этом меняется
# По измененному списку идем вновь. Возникает ошибка!
# способ работает, если в первом списке не больше 2-х одинаковых номеров
# ошибка выходит если дубли в удаляемом списке стоят более 2 раз подряд (3,4 ... и т.д. раза)
for i in list_a:
    if i in list_b:
        list_a.remove(i)
print(list_a)
# Правильный способ (вариант от переподавателя)
# если сделать срез всего списка [:] то тогда создается копия списка (для работы в цикле)
# а удаление идет уже из реального списка
for i in list_a[:]:
    if i in list_b:
        list_a.remove(i)
print(list_a)

# 4 способ мой (используется метод поверхостного копирования - copy.copy(list_a)  вместо способа list_a[:]


for i in copy.copy(list_a):
    if i in list_b:
        list_a.remove(i)
print(list_a)
# _____________________
# Практическое задание № 2
print('Практическое задание № 2')
# Вводится строковое значение даты
day = input('Введите день от 01 до 31: ')
month = input('Введите месяц от 01 до 12: ')
year = input('Введите год: ')
# Создаем словарь дней месяца
days = {'01': 'Первое', '02': 'Второе', '03': 'Третье', '04': 'Четвертое', '05': 'Пятое', '06': 'Шестое',
        '07': 'Седьмое', '08': 'Восьмое', '09': 'Девятое', '10': 'Десятое', '11': 'Одиннадцатое', '12': 'Двенадцатое',
        '13': 'тринадцатое',
        '14': 'четырнадцатое',
        '15': 'пятнадцатое',
        '16': 'шестнадцатое',
        '17': 'семнадцатое',
        '18': 'восемнадцатое',
        '19': 'девятнадцатое',
        '20': 'двадцатое',
        '21': 'двадцать первое',
        '22': 'двадцать второе',
        '23': 'двадцать третье',
        '24': 'двадцать четвертое',
        '25': 'двадцать пятое',
        '26': 'двадцать шестое',
        '27': 'двадцать седьмое',
        '28': 'двадцать восьмое',
        '29': 'двадцать девятое',
        '30': 'тридцатое',
        '31': 'тридцать первое'
        }
# Создаем словарь месяцев
months = {'01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апреля', '05': 'Мая', '06': 'Июня',
          '07': 'Июля', '08': 'Августа', '09': 'Сентября', '10': 'Октября', '11': 'Ноября', '12': 'Декабря'}

date = f'{days[day]} {months[month]} {year} года'
print(date)
print('Вы ввели следующую дату: {}.{}.{}'.format(day, month, year))
print('Ваша дата в текстовом виде: ', days[day], months[month], year, 'года')
# _____________________
# Практическое задание № 3
# удалить все повторяющиеся числа
digit_list = [1, 1, 2, 3, 3, 4, 4, 4, 5, 1, 2, 7]
result = []
for i in digit_list:
    print(i)
    if digit_list.count(i) == 1:
        result.append(i)
print(result)