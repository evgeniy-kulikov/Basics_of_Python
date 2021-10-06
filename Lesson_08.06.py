# lambda функции
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def my_filter(numbers, function):
    result = []
    for each in numbers:
        if function(each):
            result.append(each)
    return result


# если нужны четные числа
# заменяем ранее создаваемую отдельную функцию:
# def is_even(anybody):
#     return anybody % 2 == 0
# lambda-функцией
print('выборка четных чисел ', my_filter(numbers, lambda anybody: anybody % 2 == 0))
print('выборка нечетных чисел ', my_filter(numbers, lambda each: each % 2 != 0))
print('выборка числел > 4 ', my_filter(numbers, lambda big: big > 4))
