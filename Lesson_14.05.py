# Lesson_14
#
# Как работает оператор  'and'
#
# Оператор 'and' не проверяет следующее логическое выражение если текущее 'False' (ленивый)
import math

if 1 > 2 and math.sqrt(-1):  # квадратного корня из отрицательного числа несуществует - ОШИБКА
    print('Ошибки не будет т.к. первое условие ложь')
print('работаем дальше')

# для возникновения ошибки меняем условия местами
# if math.sqrt(-1) and 1 > 2:  # квадратного корня из отрицательного числа несуществует - ОШИБКА
#     print('Ошибки не будет т.к. первое условие ложь')
# print('работаем дальше')

# Оператор 'and' возвращает первый ложный элемент или последний истинный
#
# первая - ЛОЖЬ (в данном случае это '')
print([1] and 2 and '' and {3: 'b'} and [])
# последняя - ИСТИНА
# если все ИСТИНА то ператор 'and' возвращает последний истинный
print([1] and 2 and {3: 'b'} and 'три')