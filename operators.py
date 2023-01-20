####################################################################################
'''
Общий интерфейс поиска атрибутов и элементов модуля operator в Python.

Поиск атрибутов или элементов последовательностей/итераций.

Одной из самых необычных особенностей модуля operator является концепция геттеров. 
Это вызываемые объекты, созданные во время выполнения для извлечения атрибутов объектов 
или содержимого из последовательностей.

Геттеры особенно полезны при работе с итераторами или последовательностями генераторов, 
где они предназначены для быстрого извлечения полей аргументов из функций для map(), 
sorted(), itertools.groupby() или других функций, которые ожидают аргумент переданной функции.

Содержание:
 - operator.attrgetter();
 - operator.itemgetter();
 - operator.methodcaller();
 - operator.call() (добавлено в Python 3.11);
 - Примеры практического применения функции.
'''
####################################################################################
# attrgetter
print('**********attrgetter********')
'''
operator.attrgetter(attr)
operator.attrgetter(*attrs):

Функция возвращает вызываемый объект, который получает attr из своего операнда. 
Если запрашивается более одного атрибута, возвращает набор атрибутов. 
Имена атрибутов также могут содержать точки.

после f = attrgetter('name'), вызов f(b) вернет b.name.
после f = attrgetter('name', 'date'), вызов f(b) вернет (b.name, b.date).
после f = attrgetter('name.first', 'name.last'), вызов f(b) вернет (b.name.first, b.name.last).

Функция эквивалентна следующему коду:
'''
def attrgetter(*items):
    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')
    if len(items) == 1:
        attr = items[0]
        def g(obj):
            return resolve_attr(obj, attr)
    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)
    return g

def resolve_attr(obj, attr):
    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj
####################################################################################
# itemgetter
print('**********itemgetter********')
'''
operator.itemgetter(item)
operator.itemgetter(*items):

Функция возвращает вызываемый объект, который выбирает элемент из своего операнда, 
используя метод операнда __getitem__(). Если указано несколько элементов, 
возвращает кортеж значений:

после f = itemgetter(2), вызов f(r) вернет r[2].
после g = itemgetter(2, 5, 3), вызов g(r) вернет (r[2], r[5], r[3]).

Функция эквивалентна следующему коду:
'''
def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g
'''
Элементы могут быть любого типа, принятого методом операнда __getitem__(). 
Словари принимают любое хешируемое значение. Списки, 
кортежи и строки принимают индекс или срез:

>>> import operator
>>> operator.itemgetter('name')({'name': 'tu', 'age': 18})
# 'tu'
>>> operator.itemgetter(1)('ABCDEFG')
# 'B'
>>> operator.itemgetter(1,3,5)('ABCDEFG')
# ('B', 'D', 'F')
>>> operator.itemgetter(slice(2,None))('ABCDEFG')
# 'CDEFG'
>>> soldier = dict(rank='captain', name='dotterbart')
>>> operator.itemgetter('rank')(soldier)
# 'captain'
'''
import operator

print(operator.itemgetter('name')({'name': 'tu', 'age': 18})) # 'tu'

print(operator.itemgetter(1)('ABCDEFG')) # 'B'

print(operator.itemgetter(1,3,5)('ABCDEFG')) # ('B', 'D', 'F')

print(operator.itemgetter(slice(2,None))('ABCDEFG')) # 'CDEFG'

soldier = dict(rank='captain', name='dotterbart')
print(operator.itemgetter('rank')(soldier)) # 'captain'
'''
Пример использования operator.itemgetter() 
для извлечения определенных полей из записи кортежа:

>>> import operator
>>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
>>> getcount = operator.itemgetter(1)
>>> list(map(getcount, inventory))
# [3, 2, 5, 1]
>>> sorted(inventory, key=getcount)
# [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]
'''
import operator

inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
getcount = operator.itemgetter(1)
print(list(map(getcount, inventory))) # [3, 2, 5, 1]

print(sorted(inventory, key=getcount)) # [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]
####################################################################################
# methodcaller
print('**********methodcaller********')
'''
operator.methodcaller(name, /, *args, **kwargs):

Функция возвращает вызываемый объект, который вызывает имя метода в своем операнде. 
Если заданы дополнительные аргументы и/или ключевые слова, они также будут переданы методу.

после f = methodcaller('name'), вызов f(b) вернет b.name().
после f = methodcaller('name', 'foo', bar=1), вызов f(b) вернет b.name('foo', bar=1).

Функция эквивалентна следующему коду:
'''
def methodcaller(name, /, *args, **kwargs):
    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)
    return caller
####################################################################################
# call
print('**********call********')
'''
operator.call(obj, /, *args, **kwargs)
operator.__call__(obj, /, *args, **kwargs):

Функция вызывает объект obj. Если заданы дополнительные аргументы и/или ключевые слова, 
они также будут переданы методу obj(*args, **kwargs).

Добавлено в Python 3.11.
'''
####################################################################################
# example itemgetter
print('**********example itemgetter********')
'''
Примеры использования функций поиска атрибутов или элементов.

Пример практического применения функции operator.itemgetter().

from operator import *

# Для словарей
>>> l = [dict(val=-1 * i) for i in range(4)]
>>> l
# [{'val': 0}, {'val': -1}, {'val': -2}, {'val': -3}]
>>> g = itemgetter('val')
>>> [g(i) for i in l]
# [0, -1, -2, -3]
>>> sorted(l, key=g)
[{'val': -3}, {'val': -2}, {'val': -1}, {'val': 0}]

# Для кортежей
>>> l = [(i, i * -2) for i in range(4)]
>>> l
# [(0, 0), (1, -2), (2, -4), (3, -6)]
>>> g = itemgetter(1)
>>> [g(i) for i in l]
# [0, -2, -4, -6]
>>> sorted(l, key=g)
# [(3, -6), (2, -4), (1, -2), (0, 0)]
'''
from operator import *

# Для словарей
l = [dict(val=-1 * i) for i in range(4)]
print(l) # [{'val': 0}, {'val': -1}, {'val': -2}, {'val': -3}]

g = itemgetter('val')
print([g(i) for i in l]) # [0, -1, -2, -3]

print(sorted(l, key=g)) # [{'val': -3}, {'val': -2}, {'val': -1}, {'val': 0}]


# Для кортежей
l = [(i, i * -2) for i in range(4)]
print(l) # [(0, 0), (1, -2), (2, -4), (3, -6)]

g = itemgetter(1)
print([g(i) for i in l]) # [0, -2, -4, -6]

print(sorted(l, key=g)) # [(3, -6), (2, -4), (1, -2), (0, 0)]
####################################################################################
# example attrgetter
print('**********example attrgetter********')
'''
Пример практического применения функции operator.attrgetter().

from operator import *

class MyObj:
    """example class for attrgetter"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)


>>> l = [MyObj(i) for i in range(5)]
>>> l
# [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]

# Извлечем значение 'arg' из каждого объекта
>>> g = attrgetter('arg')
[g(i) for i in l]
# [0, 1, 2, 3, 4]

# теперь отсортируем, используя 'arg'
>>> l.reverse()
# [MyObj(4), MyObj(3), MyObj(2), MyObj(1), MyObj(0)]

>>> sorted(l, key=g)
# [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]
'''
from operator import *

class MyObj:
    """example class for attrgetter"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)


l = [MyObj(i) for i in range(5)]
print(l) # [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]

# Извлечем значение 'arg' из каждого объекта
g = attrgetter('arg')
print([g(i) for i in l]) # [0, 1, 2, 3, 4]

# теперь отсортируем, используя 'arg'
l.reverse() 
print(l) # [MyObj(4), MyObj(3), MyObj(2), MyObj(1), MyObj(0)]

print(sorted(l, key=g)) # [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]
####################################################################################