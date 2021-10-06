# Lesson 10
# Модуль random
#
# для импорта всего модуля "random"
# import random
#
# для импорта части модуля "random"
from random import randint, choice, sample, shuffle
#
# Загадать случайное число от 1 до 100
#
# в случае (import random)
# print(random.randint(1, 100))
#
# в случае (from random import randint)
print(randint(1, 100))
#
# выбрть случайного победителя лотереи из списка
players = ['Max', 'Leo', 'Kate', 'Tom', 'Bill', 'Alex']
print(choice(players))
# выбрть 3-x случайных победителуй лотереи из списка
print(sample(players, 3))
# перемешать карты в стопке (списке cards)
cards = ['6', '7', '8', '9', 'V', 'Q', 'K', 'T', 'J']
print(cards)
shuffle(cards)
print(cards)
