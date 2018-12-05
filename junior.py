#!-*-coding:utf-8-*-
from copy import copy, deepcopy
from decimal import Decimal

__author__ = 'virgo'

# 1. Стандартные типы данных.
is_true = True
int_number = 1
fl_num = 1.0
dec_number = Decimal()
this_str = 'Abra'
my_list = [1, 2, 3]
my_tuple = (1, 2,)
my_set = set(my_list)
my_dict = dict(a=1)

# 2. Сырые строки
print(r'asdf\n')
print('asdf\n')

# 3. Разница между tuple и list.
# Кортеж - неизменяемый, он быстрее.

# 4. Множества.
# Коллекция, содержит неупорядоченные уникальные значения. Операции, пересечения, объединение, разность.
set1 = set([1, 2, 3, 1])
set2 = {2, 3, 4}
set3 = {x for x in range(10)}  # Генератор множества
not_set = {}  # Так нельзя, будет dict
set1 |= set2  # Объединение.
set1 &= set2  # Пересечение.
set1 -= set2  # Вычитание. {1}

# 5. Стандартные биб-ки python
# json
# datetime
# os модуль для работы с ОС, причем не зависит от типа ОС.
# unittest написание и запуск тестов.
# re регулярные выражение

# 6. Что такое pep8
# Единые стиль написание кода, т.к он чаще читается, чем пишется. Автор Гуидо.

# 7. Сделать swap двух переменных.
a, b = 1, 2
a, b = b, a

# 8. Разница range (list) и xrange (возвращает генератор). Только в python 2. В третьей range == xrange.
# Генератор выгружает лишь одно число в память, а range сразу все.

# 9. Min в list.
print(min(my_list))

# 10. Удалить одинаковые элементы из списка.
print(set(my_list))

# 11. Подстроку с максимальным кол-во нулей.
s = '10000100000000000010001001'
print(max(s.split('1')))

# 12. Mutable (list, dict, set), unmutable(int, float, tuple, frozenset)

# 13. Как передаются агрументы в функцию, по ссылке или по значению.
# И так, и так.
a = 5  # По значению.
b = list()  # По ссылке


def func(a, b):
    pass


# 14. Есть ли ошибка. Да.
# print(is_none([]), is_none('')) # return True
def is_none(x):
    # if x is None:
    if x:
        return False
    return True


# 15. Отличие copy.copy и copy.deepcopy
x = [1, 2, 3]
y = x
assert id(x) == id(y)

y = copy(x)
assert id(x) != id(y)

x = [[1, 2], 1, 2]
y = deepcopy(x)
assert id(x) != id(y)

# 16. Анонимные функции.
lst = [{'a': 1}, {'b': 2}]
sorted(lst, key=lambda x: x['a'])


# 16. Private метод в python. Как таковой нет.
class A:
    _a1 = 4  # PEP8 будет недоволен, но можно.
    __a2 = 3  # Будет ошибка. Как атрибут будет A__a2


# 18. Отличии is и ==.
# is сравнивает адреса, == значения.


