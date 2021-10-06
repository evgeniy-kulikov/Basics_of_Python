# если импрот идет в пределах одной дирректории
import mod_a
import mod_c
from mod_c import foo
# если импрот идет из другой дирректории
from folder_b.mod_b import foo, bar


# вызов переменной и функции из файла "mod_a" расположенного в пределах одной дирректории "my_project"
print(mod_a.foo)
mod_a.bar()
# вызов переменной и функции из файла "mod_b" расположенного в другой дирректории "folder_b"
print(foo)
bar()
# вызов переменной и функции из файла "mod_c" расположенного в пределах одной дирректории "my_project"
print(mod_c.foo)
