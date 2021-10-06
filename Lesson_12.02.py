# Lesson_12
# Работа с файлами. Кодировки
# создание обычной строки
my_str = 'string'
print(type(my_str))
print(my_str)
# создание строки байт
my_byte = b'string byte'
print(type(my_byte))
print(my_byte)
# Действия со строками байт
# индекс sb[1]
print('индекс строки ', my_str[1])
print('индекс байт ', my_byte[1])
# срез sb[1:3]
print('срез строки ', my_str[1:3])
print('срез байт ', my_byte[1:3])
# перебор строки байт
for i in my_byte:
    print(i)

# Перевод строки в байты (кодирование)
# При переводе строки str в байты bytes указываем кодировку.
# Кодировка должна поддерживать символы нужного нам алфавита.
s = 'Hello world'
sb = s.encode('ascii')  # переводим строку в байты
print(sb)
print(type(sb))
#
s = 'Hello world мир'
sb = s.encode('utf-8')  # переводим строку в байты если в строке есть кирилица
print(sb)
#
# Перевод байт в строку (декодирование)
# Указываем кодировку, которой мы кодировали строку.
s_dec = sb.decode('utf-8')
print(type(s_dec))
print(s_dec)

