# Lesson 10
# запуск скрипта с параметрами
#
#
import sys, os
#
# список sys.argv
# print(sys.argv[0])
#
# передача параметров в скрипт
# записываем в терминале следующую строку
# python Lesson_10.06.py 123 my_lesson 3.1415
for my_arg in sys.argv:
    print(my_arg)
    print(type(my_arg))
#
# практическое задание


def ping():
    print('pong')


def hello(name):
    print('Hello', name)


# def get_info():
#     print(os.listdir())
def get_info():
    for i in os.listdir():
        print(i)


# данный скрипт для работы в терминале. В PayCharm будет ошибка
# Совет:  очистить терминал можно командой cls
#
# command = sys.argv[1]
#
# if command == 'ping':
#     ping()
# elif command == 'list':
#     get_info()
# elif command == 'name':
#     name = sys.argv[2]
#     hello(name)





