# Lesson_13 Разбор практического задания
#  2 задание
# Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. И получить объект: словарь из предыдущего задания
import json
import pickle

# открываем созданный нами файл my_group.json
with open('my_group.json', 'r', encoding='utf-8') as jc_file:
    result = json.load(jc_file)  # открытый на чтение файл загружаем в переменную
print(result)
print(type(result))
# открываем созданный нами файл my_group.pickle в режиме чтения байт
with open('my_group.pickle', 'rb') as pck_file:
    result = pickle.load(pck_file)  # открытый на чтение файл загружаем в переменную
print(result)
print(type(result))
