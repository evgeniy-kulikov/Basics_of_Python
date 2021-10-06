# Lesson 10
# Модули
import math
import random
# импортируем модуль "random" под псевдонимом "rd"
import random as rd
# импортируем весь модуль "math". НЕ РЕКОМЕНДУЕТСЯ т.к. может произойти перехлест имен
from math import*
# импортируем из модуля "random" отдельные части
from random import randint, randrange
#
#
# получаем число Пи
print('получаем число Пи', math.pi)
# получаем число Пи в случае когда "from math import*"
print('получаем число Пи в случае когда "from math import*"', pi)
# перевод из радиан в градусы
d = math.degrees(3.141592653589793)
print(d)
# Sin угла в радианах
print(math.sin(3.14))
# получаем Sin угла в радианах случае когда  " from math import* "
print(sin(3.14))
#
print('использование модуля "random" ', random.randint(1, 10))
#
print('использование модуля "random" , но под псевдонимом "rd"', rd.randint(1, 10))
#
print('использования отдельных частей из модуля "random" ', randint(1, 10))
#
print('использования отдельных частей из модуля "random" ', randrange(2, 10, 2))




