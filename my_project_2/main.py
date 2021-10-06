import random_list  # В случае если импортируется весь модуль
from folders import create_folders, delete_folders  # В случае если импортируется отдельная функция
#
# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
#
#
create_folders()
delete_folders()
print(random_list.get_random([1, 'два', 3, 'четыре', 5, 'вышел зайчик погулять']))
print(random_list.get_random([]))
