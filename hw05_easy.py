# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, sys, shutil

#  создание
for i in range(1, 10):
    path = "dir_{}".format(i)
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Директория {} уже существует".format(path))

#  удаление
for i in range(1, 10):
    path = "dir_{}".format(i)
    try:
        os.rmdir(path)
    except FileExistsError:
        print("Директория {} отсутствует".format(path))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

#  1 способ
for i in os.scandir(os.getcwd()):
    if i.is_dir():
        print(i.path)

#  2 способ
[print(i.path) for i in os.scandir(os.getcwd()) if i.is_dir()]

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

shutil.copyfile(sys.argv[0], "copycopy.py")