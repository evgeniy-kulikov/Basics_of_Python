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
    pass

# читаем как текст
with open('my_byte.txt', 'rb') as bt:
    pass

# открываем файл в текстовом режиме, с указанием кодировки
with open('my_byte.txt', 'r', encoding='utf-8'):
    pass
#
# Чтение байтов из файла
# f.read() - файл открыт в режиме r — читаем строки
# f.read() - файл открыт в режиме rb — читаем байты
