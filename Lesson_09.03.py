# Задание № 4
# Изменяем сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле: damage / armor
# Следовательно,  должно быть 2 функции:
# первая - Наносит урон. Это улучшенная версия функции из задачи 3.
# вторая - Вычисляет урон по отношению к броне.
player_name = input('Введите свое имя: ')
player = {'name': player_name,
          'health': 100,
          'damage': 50,
          'armor': 1.2
          }
enemy_name = input('Введите имя противника: ')
enemy = {'name': enemy_name,
         'health': 50,
         'damage': 30,
         'armor': 1}


def get_damage(damage, armor):
    return damage / armor


def attack(gamer, target):
    damage = get_damage(gamer['damage'], target['armor'])
    target['health'] -= damage


# атакует player (он свой)
attack(player, enemy)
print(enemy)
# атакует enemy (противник)
attack(enemy, player)
print(player)
