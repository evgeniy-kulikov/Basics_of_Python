m = 'меня видно везде'


def a():
    print('функция a()')
    ma = 'меня видно a() b() c()'
    print('внешняя переменная "m"', m)
    print('переменная функции a():', ma)
    print('- - - - - - - - - - -')

    def b():
        print('функция b()')
        mb = 'меня видно b() c() но не видно a()'
        print('внешняя переменная "m"', m)
        print('переменная "ma"', ma)
        print('переменная функции b():', mb)
        print('- - - - - - - - - - -')

        def c():
            print('функция c()')
            mc = 'меня видно c() но не видно a() b()'
            print('внешняя переменная "m"', m)
            print('переменная "ma"', ma)
            print('переменная "mb"', mb)
            print('переменная функции c():', mc)

        c()

    b()


a()
# b() и c() являются вложенными функциями для a() и поэтому их нельзя вызвать отдельно