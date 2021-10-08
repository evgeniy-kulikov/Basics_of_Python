print('* * * * * * словарь dict  * * * * * * ')
print('неупорядоченные коллекции произвольных типов с доступом по ключу')
print('my_dict = {key1:val1, key2:val2, ...}')
friends = ['Max', 'Leo', 'Kate']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))
# создаем словарь с характеристиками друзей
friend = {
    'name': 'Max',
    'age': 23,
}
print(friend)
print(type(friend))
# * * * * * * основные действия со словарем  * * * * * *
# узнаем возраст по ключу age
print(friend['age'])
# добавляем новое значение в словарь
# если такое значение уже есть, то оно заменится
friend['has_car'] = True
print(friend)
# меняем значение ключа в словаре
friend['has_car'] = False
print(friend)
# удаляем  ключ:значение  из словаря
del friend['age']
print(friend)
# работа оператора (if 'ЗНАЧЕНИЕ' in ПЕРЕМЕННАЯ ) для словаря
if 'age' in friend:
    print('есть определение возраста')
else:
    print('нет определение возраста')
if 'has_car' in friend:
    print('есть определение машины')
else:
    print('нет определение машины')
# получение элемента по ключу
# _ _ _ _ _ получение элемента по ключу _ _ _ _ _
friend = {
    'name': 'Max',
    'age': 23,
    'has car': True
}
# получаем ключи
for key in friend.keys():
    print(key)
# получаем значения
for key in friend.keys():
    print(friend[key])
# ТАК ТОЖЕ получаем ключи и их значения (другой способ)
for key in friend:
    print(key)
    print(friend[key])
# _ _ _ _ _ получаем значения ключей в словаре _ _ _ _ _
for val in friend.values():
    print(val)
# _ _ _ _ _ получаем пары  ключ:значение  в словаре _ _ _ _ _
# метод  items  возвращает список кортежа
for item in friend.items():
    print(item)
# ТАК ТОЖЕ получаем пары  ключ:значение  в словаре (другой способ)
for key, val in friend.items():
    print(key)
    print(val)