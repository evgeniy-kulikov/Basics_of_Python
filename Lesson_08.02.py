# вводим параметры  в функцию
def print_sep(space, step):
    print(space * step)


print_sep('-', 30)
print_sep('*', 30)
# пытаемся сделать возвращаемое значение в функции
result = print_sep('*', 50)
print(result)
# получим  None , т.к. результат выводится только на дисплей. А сама функция не передает никакого значения
# Переделываем функцию print_sep для получения результата


def get_sep(space, step):
    return space * step


sep = get_sep('*', 10)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)
print(get_sep('()', 10))
# параметры  функции
# hello_max  - функция без изменяемых параметров


def hello_max():
    print('Hello', 'Max')


hello_max()


# hello  - функция с одним параметром
def hello(who):
    print('Hello', who)


hello('Kate')


# greeting  - функция с двумя параметром
def greeting(who, say):
    print(say, who)


# передача параметров по порядку
greeting('Leo', 'Hi')
greeting('Max', 'Salute')
# передача параметров по имени
greeting(who='Max', say='Salute')
greeting(say='Salute', who='Max')


# значение параметров по умолчанию
def greeting(who, say='Hello'):
    print(say, who)


greeting('Max')
# значение параметра (say) по умолчанию можно изменить
greeting('Max', say='Salute')


# передача параметров по порядку
# звездочка "*" перед параметром "args" дает возможность передать несколько параметров (аргументов)
#   *args  принятый стандарт написания
#   с аргументом *args  мы получаем КОРТЕЖ
def welcome(say, *args):
    print(say, args)


welcome('salute', 'Max', 'Leo', 'Kate', 'Nick')


#   *kwargs  пераметр
#   с аргументом *kwargs  мы получаем СЛОВАРЬ
def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age=25)
print('_ _ _ _ _ количество параметров можно увеличивать (образуется СЛОВАРЬ)_ _ _ _ _')
get_person(name='Leo', age=25, has_car=True)
