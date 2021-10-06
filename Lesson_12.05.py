# Lesson_12
# Работа с файлами.
# Работа с файлом в режиме байтов
# открываем файл для записи байтов
with open('my_byte.txt', 'bw') as bt:
    str_my = 'Привет мир байт'  # пишем строку
    bt.write(str_my.encode('utf-8'))  # даем нужную кодировку

print('')

with open('my_byte.txt', 'w', encoding='utf-8') as st:
    st.write('Привет мир строк')  # пишем строку

# открываем файл в режиме чтения файлов
with open('my_byte.txt', 'br') as bt:
    result = bt.read()
    print(result)
    print(type(result))
    bt_encode = result.decode('utf-8')
    print(bt_encode)
    print(type(bt_encode))



