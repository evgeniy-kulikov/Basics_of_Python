# Lesson_14
# Генераторы списков
#
# Примеры
import random
# Создать список из случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# Создать список квадратов чисел
numbers = [1, 2, 3, -4]
number = [i**2 for i in numbers]
print(number)
# Создать список имен на букву А
names = ['Руслан', 'Алексей', 'Дмитрий', 'Андрей', 'Олег']
name = [i for i in names if i.startswith('А')]
print(name)
