#
# Lesson_12
# Работа с файлами. Кодировки
#
# Функция open
# Режимы открытия (mode)
#
# w — запись, если файла нет, создается новый
# x — запись, если файла нет, ошибка
# a — дозапись
# r — чтение
# b — двоичный режим
# + — открытие на чтение и запись
#
# file — имя файла
# mode — режим
# открывает файл в указанном режиме
#
f = open('my_first.txt', 'w')  # файл создается в данном проекте
print(type(f))  # <class '_io.TextIOWrapper'>
#
# Запись текста в файл
# writelines — записать список строк в файл
# \n — символ конца строки
# write — записать строку в файл
# Если текст в файле был, то он перезаписывается
f.write('First line\nsecond line')  # без \n текст сливается в одну строку
f.write('\nthird line')
f.write('\n')
f.write('fourth line\n')
# write — записать строку в файл списком
f.writelines(['5 line\n', '6 line\n'])
#
# Чтение из файла
# for line in f: — чтение файла построчно
# readlines — чтение файла в список строк
# read — чтение всего файла
f = open('my_first.txt', 'r')
print(f.read())
#
# Чтение из файла
# for line in f: — чтение файла построчно
f = open('my_first.txt', 'r')
for line in f:
    print(line.replace('\n', ''))  # для удаления переноса строки, ведь цикл его тоже печатает


# readlines — чтение файла в список строк
f = open('my_first.txt', 'r')
print(f.readlines())
#
# Закрытие файла
# Открытые файлы тратят ресурсы системы
# f.close()
# Если до close произойдет исключительная ситуация, файл не будет закрыт.
# Удобным вместо close() является использование конструкции " with "
f = open('my_first.txt', 'r')
with open('my_first.txt', 'r'):
    print(f.readlines())
print(f.readlines())

