# Lesson 10
# Модуль sys
#
import sys
#
# путь до интерпретатора
print('где находится файл "python.exe"? ', sys.executable)
#
# информация о платформе
print(sys.platform)
# win32
#
# выход из Python
# sys.exit()
# print('эта строчка уже не выполнится')
#
print(type(sys.path))
print(sys.path)
# для удобства чтения выводим список построчно
for i in sys.path:
    print(i)
# внесем новый путь для переменной на другом диске (файл "my_python_module.py" на диске I:)
sys.path.append('D:\_path')
import my_python_module