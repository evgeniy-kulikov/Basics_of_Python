# Задание № 3
# Давайте опишем пару сущностей: player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100, (здоровье)
# damage = 50.  (урон, повреждение)
# Теперь надо создать функцию attack(person1, person2).
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения
player_name = input('Введите свое имя: ')
player_a = {'name': player_name,
            'health': 100,
            'damage': 50
            }
print('исходные данные игрока', player_name, player_a)
enemy_name = input('Введите имя противника: ')
player_b = {'name': enemy_name,
            'health': 50,
            'damage': 30
            }
print('исходные данные игрока', enemy_name, player_b)


def attack(gamer, target):
    target['health'] -= gamer['damage']


# атакует player (он свой)
attack(player_a, player_b)
print(player_b)
# атакует enemy (противник)
attack(player_b, player_a)
print(player_a)
