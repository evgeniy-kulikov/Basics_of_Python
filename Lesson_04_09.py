print('* * * * * * множества  set * * * * * * ')
cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
print(cities)
print(type(cities))
# преобразуем список в множество
cities = set(cities)
print(cities)
print(type(cities))
# добавляем новый элемент
cities.add('Burma')
print(cities)
# добавляем ПОВТОРЯЮЩИЙСЯ элемент (ничего не происходит)
cities.add('Paris')
print(cities)
# удаляем  элемент
cities.remove('Las Vegas')
print(cities)
# применяем метод последовательности. Например определение длины
print(len(cities))
# проверка наличия элемента
print('Paris' in cities)
# перебор элементов множества через метод  for
for city in cities:
    print(city)
print('_ _ _ _ _ операции со множеством _ _ _ _ _')
# Супруги Max и Kate собирвют вещи в поездку.
# Max взял такие вещи:
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты', 'Удочка'}
# Kate взяля другие вещи:
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}
# Какие вещи взяли супруги вместе?
# Объединение множеств через  " |  "
print(max_things | kate_things)
# Какие вещи повторяются?
# Пересечение множеств через  " &  "
print(max_things & kate_things)
# Какие вещи взял только Max, но не взяла Kate?
# Из вещей Max вычетаем вещи Kate
print(max_things - kate_things)
# Какие вещи взяла только Kate, но не взял Max?
print(kate_things - max_things)
