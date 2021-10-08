# 04.3
# Списки, определения, методы
# Списки (List)
# Списки - упорядоченые ИЗМЕНЯЕМЫЕ коллекции объектов ПРОИЗВОЛЬНЫХ типов
# som_list = ['hello', 123, True]
#
# объявляем пустой список
empty_list = []
print(empty_list)
# []
# объявляем новый заполненный список
friends = ['Max', 'Leo', 'Kate']
print(friends)
# ['Max', 'Leo', 'Kate']
print(type(friends))
# <class 'list'>
# Как и в сторке, для списка доступны индексы (начиная с  " 0 ")
print('второй друг в списке:', friends[1])
# второй друг в списке: Kate
print('первый друг с конца списка:', friends[-1])
# первый друг с конца списка: Kate
# В списке пожно применять СРЕЗЫ
print(friends[1:2])
# ['Leo']
print(friends[:2])
# ['Max', 'Leo']
print(friends[1:])
# ['Leo', 'Kate']

# функция len  и методы списка
# объявляем новый заполненный список
friends = ['Max', 'Leo', 'Kate']
print(friends)
# узнаем колличество элементов в списке
print(len(friends))
# 3
# добавляем новый элемент в КОНЕЦ списка
friends.append('Ron')
print(friends)
# ['Max', 'Leo', 'Kate', 'Ron']
print(len(friends))
# 4
# удаляем последний элемент в списке. Одновременно его можно вывести в печать.
print(friends.pop())
# Ron
print(friends)
# ['Max', 'Leo', 'Kate']
# Очищаем весь список
friends.clear()
print(friends)
# []
friends = ['Max', 'Leo', 'Kate']
# удаляем элемент из списка по ЗНАЧЕНИЮ
friends.remove('Kate')
print(friends)
# ['Max', 'Leo']
# удаляем элемент из списка по ИНДЕКСУ
del friends[0]
print(friends)
# ['Leo']
