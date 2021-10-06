# Lesson 10
# Модуль math
import math
#
# простые задачи
#
# найти длину окружности с определенным радиусом r = 10
r = 10
print(2*r*math.pi)
#
# найти площадь окружности с определенным радиусом r = 10
print((r**2)*math.pi)
# тоже самое, но для возведения в степень используем из библиотеки math модуль math.pow(X, Y) - где Y степень
print((math.pow(r, 2))*math.pi)
#
# по координатам 2-х точек найти расстояние "l" между ними
x1 = 10
y1 = 10
x2 = 50
y2 = 100
l1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(l1)
l2 = math.sqrt((math.pow((x2 - x1), 2)) + math.pow((y2 - y1), 2))
print(l2)
#
# найти факториал числа 9
print(math.factorial(9))
print(math.factorial(0))
print(math.factorial(1))

