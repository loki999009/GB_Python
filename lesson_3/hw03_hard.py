__author__ = 'Садовой Андрей Андреевич'

import re


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def search_nod(a, b):

    '''Нахождение нибольшего общего делителя для чисел а и b'''

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def search_nok(a, b):

    '''Нахождение наименьшего общего кратного для чисел а и b'''

    return a * b / search_nod(a, b)


def diff(lst):
    '''Вычисление разности элементов списка'''
    difference = lst[0]
    for x in range(len(lst)):
        if x:
            difference = difference - lst[x]
    return difference


def format_dec(num, NOK):

    '''выделение целой части дроби'''

    if num > NOK:
        cel = num // NOK
        new_num = num % NOK
        result = '{0:.0f} {1:.0f}/{2:.0f}'.format(cel, new_num, NOK)
    else:
        result = '{0:.0f}/{1:.0f}'.format(num, NOK)
    return result

print('-' * 50)

print('Задача 1')

equation = '7/17 - -5'

# получаем все дроби из строки

params = re.findall(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)

# получаем список содержащий оператор

funcs = re.split(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
nums = []
noms = []
i = 0
for param in params:
    temp = param.split('/')
    nums.append(int(temp[0]))
    if len(temp) > 1:
        noms.append(int(temp[1]))
    else:
        noms.append(1)
for p in funcs:
    # определяем оператор действия с дробями
    if p:
        func = p.strip()
        break
NOK = search_nok(noms[0], noms[1])
for n in nums:
    # вычисляем новые числители по найденному НОК
    nums[i] = n * NOK / noms[i]
    i += 1
print('Результат вычисления ' + equation + ':')
if func == '+':
    print(format_dec(sum(nums), NOK))
elif func == '-':
    print(format_dec(diff(nums), NOK))
else:
    print('Действие не определено')


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def select(x):
#функция рассчитывает зарплату по часам согласно условию
    mani, clock, real_clock = list(map(int, x))
    if clock > real_clock:
        res = mani / clock * real_clock
    else:
        res = mani + (mani / clock * real_clock - clock) * 2
    return int(res)


with open('workers.txt', encoding='utf-8') as inp, open('hours_of.txt', encoding='utf-8') as clock:

    #получаем 2 списка list_norm- список полных данных, list_real-список имя фам. и отработанных ч.

    list_norm = inp.read().split('\n')
    list_real = clock.read().split('\n')


def name_data(x):

#получаем из строки упорядоченные данные имя фамилия и список [ зарпл. нормо_часы]

    x = x.split()
    name, mani, clock = ' '.join(x[:2]), x[2], x[4]
    return name, [mani, clock]


full_data = dict()

#так как порядок следования имя-фам в файлах разный создаем словарь из первого файла 
#полных данных с ключами из имен с фамилией и значением-список из зарплаты и нормачасов

for x in list_norm[1:]:
    name, data = name_data(x)
    full_data[name] = data
for i in list_real[1:]:

#читаем второй список с именами и отработанными часами, получаем имя фамил. и добавляем в
#словарь по ключу(имя фамил.) в значение-список реально отраб. часы

    i = i.split()
    full_data[' '.join(i[:2])].append(i[-1])

with open('data_cvit_of_price.txt', 'w', encoding='utf-8') as out:
    out.write('Имя Фамилия  Зарплата  Норма_часов  Отработано  К выдаче\n')

#берем человека и его данные обрабатываем и пишем в файл
    for name in full_data:
        out.write('{}  {}  {}  {}   {}\n'.format(name, *(full_data[name]), select(full_data[name])))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

def write_in_file(name, lst):
    '''Выполняет открытие файла с переданным именем, если файла в директори нет
    создает новый файл. После записи в файл элементов списка закрывает файл.'''
    file_name = 'data/fruits_' + name + '.txt'
    file = open(file_name, 'w', encoding='utf-8')
    for n in lst:
        file.write(n)
    file.close()
print('-' * 50)
print('Задача 3')
first_liter = ''
count = 0
temp = []
fruits = open('data/fruits.txt', 'r', encoding='utf-8')
for line in fruits:
    if (line[0] != first_liter) & (count == False):
        first_liter = line[0]
    elif line[0] == first_liter:
        name = line[0]
        temp.append(line)
    else:
        write_in_file(name, temp)
        first_liter = line[0]
        temp = []
        temp.append(line)
        if name != line[0]:
            name = line[0]
    count += 1
write_in_file(name, temp)
print('Формирование файлов по именам фруктво закончено!')