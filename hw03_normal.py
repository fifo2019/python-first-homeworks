# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    f = [1, 1]
    while len(f) < m:
        f.append(f[-1] + f[-2])
    return f[n - 1:m]


print(fibonacci(3, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    i = 1
    while i < len(origin_list):
        if i == 0 or origin_list[i - 1] <= origin_list[i]:
            i += 1
        else:
            origin_list[i - 1], origin_list[i] = origin_list[i], origin_list[i - 1]
            i -= 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filt(lst, pred):
    return [i for i in lst if pred(i)]


print(filt([2, 10, -12, 2.5, 20, -11, 4, 4, 0], lambda x: x < 4))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def parallelogram(a1, a2, a3, a4):
    a, b, c, d = sorted([a1, a2, a3, a4])
    return a[1] == c[1] and b[1] == d[1] and d[0] - b[0] == c[0] - a[0] and b[0] - a[0] == d[0] - c[0]


print(parallelogram((0,0), (1,2), (5,0), (6,2)))

