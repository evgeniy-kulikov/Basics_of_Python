import random


def get_random(input_list):
    if input_list:  # если наш список не пустой, то...
        result_list = random.choice(input_list)  # делаем случайный выбор в переменной "input_list"
        return result_list  # возвращаем случайно выбранный элемент


if __name__ == '__main__':  # блокировка выполнения данных функций в модуле main.py
    print(get_random([1, 2, 3, 4, 5]))
    print(get_random(['раз', 'два', 3, 'четыре', 'пять']))
    print(get_random([]))  # если список пустой, то должно вернуть "None"
