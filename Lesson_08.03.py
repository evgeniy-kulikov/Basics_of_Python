# зоны видимости для функции
print('_ _ _ _ _ зоны видимости для функции _ _ _ _ _')


def zone_f():
    a = 777
    print('Переменная функции:', a)


a = 1
zone_f()
print('Переменная после функции:', a)
# глобальные переменные
print('_ _ _ _ _ глобальные переменные _ _ _ _ _')
outside_var = 1


def my_f():
    global outside_var
    local_var = 100
    print(outside_var)
    print(local_var)
    outside_var = 'сторка'



my_f()
print(outside_var)
# после запуска функции с использованием глобальной переменной она изменится и в других местах!!!
# print(outside_var + 5)        # !!! ОШИБКА (строка + число) !!!
