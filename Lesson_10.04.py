# Lesson 10
# Модуль os
#
import os
# имя операционной системы
print(os.name)
#
# текущая рабочая директория
print(os.getcwd())
#
# создаем новый путь
new_path = os.path.join(os.getcwd(), '_new_aaa')
#
# создаем папку по новому пути
os.mkdir(new_path)
print(os.path.supports_unicode_filenames)