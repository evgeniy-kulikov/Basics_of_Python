# Lesson_12
# Способы записи объекта в файл
# ручной способ (создание велосипеда)
#
# наш словарь
# person = {'name': 'Max', 'phones': [123, 345]}
#
# читаем объект из файла
with open('person.dat', 'rb') as f:
    # прочитаем файл в список
    result = f.readlines()

# воссоздаем исходный объект
person = {}
# первый элемент это имя
person['name'] = result[0].decode('utf-8').replace('\n', '')
# далее два элемента это телефоны
phone_dic = []
for i in result[1:]:
    phone_dic.append(i.decode('utf-8').replace('\n', ''))

person['phones'] = phone_dic
print(person)
