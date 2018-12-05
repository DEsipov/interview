import datetime as dt


# 18. Переменная по умолчанию.
def foo(time=dt.datetime.now()):
    print(time)


print(foo())
print(foo())
print(foo())

# Везде напечатает одинаковое значение, потому что default значение присваиваются, при определении функции.


# 17. Переменная по умолчанию будет сохраняться в памяти.
def f(x, a=[]):
    a.append(x)
    print(a)


f(2)     # [2]
f(2, 4)  # [2, 2]
f(3, [1, 2])    # [1, 2, 3]


# 19. Generator.

# Генераторная функци возвращает генератор на каждой итерации.
def fibonacci():
    """
    for x in fibonacci():
    print(x)
    if x > 15:
        break
    :return:
    """
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur


# Генераторное выражение.
lst = [x for x in range(3)]


# 20. Итератор. Объекты, элементы которых можно перебирать в цикле for, содержат в себе объект итератор,
class SimpleIterator:
    """
    itr = SimpleIterator(3)
    print(next(itr))    # 1
    print(next(itr))    # 2
    """
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


# 21. Что напечатается
def f(*args, **kwargs):
    """
    f(*[1, 2, 3])
    >(1, 2, 3) {}
    :return:
    """
    print(args, kwargs)


# 23. Какой результат выполнения.
a = dict(one=1, two=2)
keys = a.keys()
a['four'] = 4
print(keys)
# ['one', 'two'] a.keys() => возвращает неизменяемый объект.


# 24. В чем разница в выполнении
d = dict(zip(range(50000000), range(50000000)))
keys1 = list(d)
keys2 = d.keys()
print(49999999 in keys1)
print(49999999 in keys2)
key3 = d
