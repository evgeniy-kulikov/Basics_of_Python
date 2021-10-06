# Lesson_12
# Модуль json в Python. Применение.
#
# Формат json
import json

friends = [{'name': 'Max', 'age': 23, 'phones': [123, 456]},
           {'name': 'Leo', 'age': 33}]

print(friends)
print(type(friends))
#
# открываем файл
with open('friends.json', 'w') as fr_js:
    # преобразуем список friends в формат json и  сохраняем в файл
    json_friends = json.dump(friends, fr_js)
#
# обратно из файла в объект
with open('friends.json', 'r') as fr_js:
    friends = json.load(fr_js)
print(friends)
print(type(friends))
