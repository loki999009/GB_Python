__author__ = 'Садовой Андрей Андреевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]
#    fib = [1, 1]
#    i = 2
#    while i <= m-1:
#        fib.append(int(fib[i-2]) + int(fib[i-1]))
#        i += 1
#    return fib[n-1:]



n = int(input("Введите первое число ряда "))
m = int(input("Введите второе число ряда "))
fibonacci(n, m)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list), 0, -1):
        for j in range(1, i):
            if origin_list[j - 1] > origin_list[j]:
                tmp = origin_list[j - 1]
                origin_list[j - 1] = origin_list[j]
                origin_list[j] = tmp
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_func(function, iterable):
    return (item for item in iterable if function(item))


print(list(filter_func(lambda x: True if x % 3 == 0 else False,
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(a, b, c, d):
    if abs(c[0] - b[0]) == abs(d[0] - a[0]) and \
       abs(b[1] - a[1]) == abs(c[1] - d[1]):
        return True
    return False

a = [-10, -20]
b = [-10, 20]
c = [10, 20]
d = [10, -20]
print(is_parallelogram(a, b, c, d))
