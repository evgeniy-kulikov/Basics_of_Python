# Lesson_12
# Модуль json в Python. Применение.
#
# Формат json
# Текстовый формат обмена данными, основанный на JavaScript.
# JavaScript Object Notation.
# Аналогичен набору словарей, списков, простых типов данных в Python.
# Является просто текстом (строкой).
import json

# создадим сложный список состоящий из словарей
friends = [{'name': 'Max', 'age': 23, 'phones': [123, 456]},
           {'name': 'Leo', 'age': 33}]
print(friends)
print(type(friends))
#
# преобразуем список friends в json
json_friends = json.dumps(friends)
# сложный список превратился в строку
print(json_friends)
print(type(json_friends))
#
# обратно из json в объект
#
friends = json.loads(json_friends)
print(type(friends))
