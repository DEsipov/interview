#!-*-coding:utf-8-*-
__author__ = 'virgo'


# Удалить все элементы списка.
lst = [1, 2]
del lst[:]
print(lst)

# Создать копию списка.
lst2 = lst[:]

# Анотация типов.
def pow(a: int, b: int) -> int:
    return a * b
print(pow(3, 4))


# Объединить два словаря.
a = {'a': 1}
b = {'b': 2}
res = {**a, **b}

