# Lesson_14
#
# Приведение типов к bool в Python
#
# Истина: ‘abc’, [1], (1,), {1:’a’}, 10, 1.1, ...
# Ложь: ‘’, [], (), {}, 0, None, ...
#
# стандартный способ
# берм строку
s = 'abc'
# s = ''
if len(s) != 0:
    print('строка не пустая')
else:
    print('строка пустая')

# удобный Python способ
if s:
    print('строка не пустая')
else:
    print('строка пустая')

# берем список и словарь
l = [1, 2, 3]
d = {1: 'a'}
# стандартный способ
if len(l) != 0 and len(d) != 0:
    print('список и словарь не пустые')
else:
    print('список и словарь пустые')

# удобный Python способ
if l and d:
    print('список и словарь не пустые')
else:
    print('список и словарь пустые')
