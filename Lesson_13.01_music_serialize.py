# Lesson_13 Разбор практического задания
#  1 задание
# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
import json
import pickle

my_favourite_group = {'name': 'Александр Иванов', 'tracks': ['Московская осень', 'Моя неласковая Русь'],
                      'albums': [{'name': 'Лучшее', 'year': 2008}, {'name': 'Это Был Я', 'year': 2011}]}
print(my_favourite_group)
print(type(my_favourite_group))
# загружаем словарь в файл формата json
js_group = json.dumps(my_favourite_group)
print(js_group)
print(type(js_group))
# загружаем словарь в виде байтов с помощью модуля pickle
pck_group = pickle.dumps(my_favourite_group)
print(pck_group)
print(type(pck_group))
# открываем создание и запись файла в формате json
with open('my_group.json', 'w', encoding='utf-8') as jc_file:
    json.dump(my_favourite_group, jc_file)
# открываем создание и запись файла с помощью модуля pickle
# т.к. запись идет в формате байт, то кодировку указывать не надо
with open('my_group.pickle', 'wb') as pck_file:
    pickle.dump(my_favourite_group, pck_file)

