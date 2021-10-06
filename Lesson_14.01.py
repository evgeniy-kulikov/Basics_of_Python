# Lesson_14
# Тернарный оператор

# тернарный (ternarius — «тройной») оператор — операция, возвращающая свой первый или третий операнд
# в зависимости от значения логического выражения, заданного вторым операндом
# результат 1 если выражение_истинно, иначе результат 2

# Синтаксис
# number = 1 if is_one else 2
# в общем виде: результат1 если условие иначе результат2

is_has_name = True
name = 'Max' if is_has_name else 'Empty'
print(name)

is_one = False
number = 1 if is_one else 2
print(number)

is_russian = True
print('Привет' if is_russian else 'Hello')

# Примеры использования
#
# от if к тернарному оператору
# слово -> СлОвО
word = 'слово'
result = []  # создаем пустой список
for i in range(len(word)):  # строим числовой ряд (длина ряда равна кол-ву букв в переменной "word")
    if i % 2 == 0:  # если число ряда делится без остатка на 2 (т.е. оно четное)
        letter_word = word[i].upper()  # задаем верхний регистр
    else:
        letter_word = word[i].lower()  # иначе (т.е. оно нечетное), задаем нижний регистр
    result.append(letter_word)  # добавляем в результирующий список полученные буквы
result = '_'.join(result)  # из полученного списка ['С', 'л', 'О', 'в', 'О'] делаем строчку (<class 'str'>)  СлОвО
# пусые кавычки '' дают отсутствие примежутков (или других символов) между буквами в строчке
print(result)


# то же самое, но с использованием тернарного оператора
result = []
for i in range(len(word)):
    letter_word = word[i].upper() if i % 2 == 0 else word[i].lower()
    result.append(letter_word)
result = ''.join(result)
print(result)

# то же самое, но немного упростим
# заменим   word[i]  на    w
result = []
for i in range(len(word)):
    w = word[i]
    letter_word = w.upper() if i % 2 == 0 else w.lower()
    result.append(letter_word)
result = ''.join(result)
print(result)
print(type(result))

# проверка пароля пользователя
password = input('Введите пароль: ')
print('Войти' if password == 'secret' else 'Вход запрещен')
