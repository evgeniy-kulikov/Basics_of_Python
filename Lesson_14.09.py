# Lesson_14
#
# Обработка исключений
#
# Исключительная ситуация
# Во время выполнения программы могут возникать ситуации, когда состояние внешних данных, устройств ввода-вывода
# или компьютерной системы в целом делает дальнейшие вычисления в соответствии с базовым алгоритмом невозможными
# или бессмысленными
#
# Классические примеры:
# Ошибка чтения данных при отсутствии доступа к ресурсу
# Деление на 0
# другие случаи ...
number = int(input('введите число: '))
result = 100 / number
print('дальнейшие действия')
# если введем строку или ноль, то выполнение программы остановится и 'дальнейшие действия' не выполнятся
number = int(input('введите число: '))

# Обработка исключений
#     Блок с возможной исключительной ситуацией
# try:
# except:
#     Код, который выполняется при возникновении исключительной ситуации.

try:
    result = 100 / number
except:
    print('нельзя вводить ноль')


print('дальнейшие действия')
#
# Перехват конкретных исключений
# TypeError, ValueError, ...
# Самое общее исключение имеет тип Exception.
# В Python каждая исключительная ситуация имеет свой тип.
# Рекомендуется обрабатывать конкретные исключительные ситуации и реагировать на разные исключения по-разному
number = int(input('введите число: '))

try:
    result = 100 / number
except ZeroDivisionError:
    print('нельзя вводить ноль')
except Exception:
    print('неизвестная ошибка!')

print('дальнейшие действия')

# Информация об ошибке
# Тогда в переменную e будет сохранен объект исключения.
# Можно получить дополнительную информацию об исключении,Если использовать конструкцию except Исключение as e:
number = int(input('введите число: '))

try:
    result = 100 / number
except ZeroDivisionError as e:
    print('нельзя вводить ноль')
    print('информация об исключении', e)
except Exception as e:
    print('неизвестная ошибка!')
    print('информация об исключении', e)

print('дальнейшие действия')

# try - except - else - finally
#
# Блок except — что делать при возникновении исключения.
# Блок else — что делать, если исключения не произошло.
# Блок try — код, который может вызвать исключение.
# Блок finally — выполняется всегда

number = int(input('введите число: '))

try:
    result = 100 / number  # код, который может вызвать исключительную ситуацию
except:   # что делать при возникновении исключительной ситуации
    print('нельзя вводить ноль')
else:  # что делать если ошибок не было
    print('ошибок не было')
finally:  # выполняется всегда
    print('выполняем работу, когда есть ошибка и когда ее нет')

print('дальнейшие действия')