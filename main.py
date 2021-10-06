# Для урока
# Практикум.
#
# from hospital.h import get_main
# from hospital.patients.index import get_index
#
#
# get_main()
# get_index()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# Для урока 16
# Практикум. File Manager.

import sys
from core import create_file, create_folder, get_list_dir, delete_file, copy_file, save_info, change_dir
from Lesson_17_01_game_normal import game_normal
from Lesson_17_03_game_multi import game_multi

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. Для справки введите help: ')
else:
    if command == 'get_list':
        get_list_dir(True)
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            create_folder(name)
    elif command == 'delete_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            delete_file(name)
    elif command == 'copy_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести название файла и название копии')
        else:
            new_name = sys.argv[3]
        copy_file(name, new_name)
    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        except FileNotFoundError:  # метод не срабатывает. Решение не найдено!!!
            print('Такой директории не существует')
        else:
            change_dir(name)
    elif command == 'help':
        print('get_list - Просмотр списка файлов и папок')
        print('create_file - Создание файла')
        print('create_folder - Создание папок')
        print('delete_file - Удаление файлов и папок')
        print('copy_file - Копирование папки и файлов')
        print('change_dir - Изменит текущую директорию')
    elif command == 'game':
        game_normal()
    elif command == 'game_multi':
        game_multi()

save_info('Конец')
