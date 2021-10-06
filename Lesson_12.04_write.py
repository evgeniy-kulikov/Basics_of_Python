# Lesson_12
# Работа с файлами.
# Работа с файлом в режиме байтов
#
# open(‘filename’, ‘rb’) — режим чтения байтов
# параметр encoding определяет кодировку
# open(‘filename’, ‘wb’) — режим записи байтов
# open(‘filename’, ‘w’, encoding=’utf-8’)
#
# открываем файл для записи байтов
with open('my_byte.txt', 'wb') as bt:
    bt.write(b'Hello bytes')  # пишем строку байт

# читаем как текст (преобразуем байты в строку)
with open('my_byte.txt', 'r', encoding='ascii') as bt:
    print(bt.read())

# открываем файл для записи байтов
with open('my_byte.txt', 'bw') as bt:
    my_srt = 'Привет мир байт'  # пишем строку
    bt.write(my_srt.encode('utf-8'))  # даем нужную кодировку

# читаем как текст с кодировкой utf-8
with open('my_byte.txt', 'r', encoding='utf-8') as bt:
    print(bt.read())
