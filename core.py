# Lesson_16
# Практикум.
# File Manager
# Создание скрипта


import os
import shutil  # для возможности копирования файла или папки
import datetime  # для работы с датой/временем


# Создание файла


def create_file(name, text=None):  # фунуция для создания файла "name" и записи в нег текста "text"
    with open(name, 'w', encoding='utf-8') as f:  # открываем файл для записи как переменную  " f "
        if text:  # если текст есть, то...
            f.write(text)  # записываем текст в созданный файл


# При создании функции "def create_folder(name):" для создания папки нужно учесть, что
# при повторном запуске функции "create_folder('new_folder ')"
# будет ошибка "Невозможно создать файл, так как он уже существует"
# поэтому делаем обработку исключения ошибки

# Создание папок


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')


# Просмотр списка файлов и папок


def get_list_dir(folders_only=False):
    result = os.listdir()
    if folders_only:  # если значение  " True "...
        result = [i for i in result if os.path.isdir(i)]  # ..то перебор всех элементов директории и показ только папок
    print(result)


# Удаление файлов и папок


def delete_file(name):
    if os.path.isdir(name):  # если это имя папки...
        os.rmdir(name)  # ...то папку удаляем
    else:
        os.remove(name)


# Копирование папки и файлов


def copy_file(real_name, new_name):
    if os.path.isdir(real_name):
        try:
            shutil.copytree(real_name, new_name)
        except FileExistsError:
            print('Папка с таким именем уже существует')
    else:
        shutil.copy(real_name, new_name)


# Запись информации о работе менеджера в файл


def save_info(message):
    current_time = datetime.datetime.now()  # текущая дата и время
    result = f'{current_time} - {message}'
    with open('text_time.txt', 'a', encoding='utf-8') as f_time:  # открываем файл на запись
        f_time.write(result + '\n')


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())


# для того что бы при импорте этих функций в другой скрипт, эти нижерасположенные функции не выполнялись
if __name__ == '__main__':
    create_file('text.dat', 'any text ')  # создали файл
    create_folder('new_folder')  # создали папку
    create_folder('new_folder_1')  # создали папку
    get_list_dir()  # все содержимое (файлы и папки)
    get_list_dir(True)  # только папки
    delete_file('new_folder_1')  # удалаяем папку
    delete_file('text.dat')  # удалаяем файл
    copy_file('new_folder', 'new_folder_copy')
    create_file('text.dat', 'any text ')  # снова создали файл
    copy_file('text.dat', 'text_copy.dat')  # копируем файл
    save_info('Пора учиться!')

