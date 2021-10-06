# Lesson_14
#
# оператор  or
# сохранение в переменную одного из 2-х значений
# создаем функцию добавление элемента в список
def add_to_list(input_list=None):
    if input_list is None:
        input_list = []
    input_list.append(2)
    return input_list


result = add_to_list([0, 1])
print(result)

result = add_to_list()
print(result)

# получаем аналогичный результат с использование оператора  'or'


def add_list_or(input_list=None):
    #  используем свойство  'or'  вместо условия
    input_list = input_list or []
    input_list.append(2)
    return input_list


result = add_to_list([0, 1])
print(result)

result = add_to_list()
print(result)
