def some_f():
    return 10


a = some_f()
print(a)
print(type(a))


def f():
    print('hello from other "f"')


def to(f_param):
    f_param()


# параметром будет функция  "f"
# поэтому в теле функции "to" мы её вызовем
to(f)


# простая (однозначная) функция для фильтрации списка четных чисел
def my_filter(numbers):
    result = []
    for k in numbers:
        if k % 2 == 0:
            result.append(k)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print('функция только для четных чисел ', my_filter(numbers))
# изменяем функцию для фильтрации списка чисел по произвольным условиям
# для этого передаем параметром другую функцию делающую нужную выборку


def my_filter(numbers, function):
    result = []
    for each in numbers:
        if function(each):
            result.append(each)
    return result


# если нужны четные числа
def is_even(anybody):
    return anybody % 2 == 0


print('выборка четных чисел ', my_filter(numbers, is_even))
# если нужны нечетные числа


def is_not_even(anyone):
    return anyone % 2 != 0


print('выборка нечетных чисел ', my_filter(numbers, is_not_even))
# если нужны числа > 4


def is_big_4(big):
    return big > 4


print('выборка числел > 4 ', my_filter(numbers, is_big_4))