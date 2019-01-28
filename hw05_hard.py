# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        shutil.copyfile(dir_name, "copy" + dir_name)
        print("Копирование завершино")
    except:
        print("Не удалось скопировть")


def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    print("Вы уверены? Y/N")
    if input().upper() != "Y":
        return
    try:
        os.remove(dir_name)
        print("Файл удален")
    except:
        print("Удалить не удалось")


def change_dir():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print("Директория изменена")
    except:
        print("Не удалось сменить директорию")


def full_name():
    print(os.path.abspath(os.curdir))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": full_name
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
else:
    print("Ключ не задан")