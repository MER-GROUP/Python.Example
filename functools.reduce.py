####################################################################################
'''
Синтаксис:
from functools import reduce
reduce(function, iterable[, initializer])

Параметры:
function - пользовательская функция, принимающая 2 аргумента,
iterable - итерируемая последовательность,
initializer - начальное значение.

Возвращаемое значение:
требуемое единственное значение.

Описание:
Функция reduce() модуля functools кумулятивно применяет функцию function 
к элементам итерируемой iterable последовательности, сводя её к единственному значению.

function это это функция которую требуется применить к элементам последовательности. 
Должна принимать два аргумента, где первый аргумент - аккумулированное ранее значение, 
а второй аргумент следующий элемент последовательности.

iterable представляет собой последовательность, 
элементы которой требуется свести к единственному значению. 
Если последовательность пуста и не задан аргумент initializer, 
то возбуждается исключение TypeError.

Например reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
вычисляет ((((1 + 2) + 3) + 4) + 5). 
Левый аргумент x - это накопленное значение, 
а правый аргумент y - это следующий элемент iterable.

Если присутствует необязательный initializer, 
он помещается перед элементами iterable в вычислении. 
Другими словами это базовое значение, с которого требуется начать отсчёт. 
Аргумент initializer, так же служит значением по умолчанию, 
когда iterable является пустым.
'''
####################################################################################
# Функция reduce() эквивалентна следующему коду:
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
####################################################################################
# Вычисление суммы всех элементов списка при помощи reduce
print('**********Вычисление суммы всех элементов списка при помощи reduce********')
from functools import reduce
items = [10, 20, 30, 40, 50]
sum_all = reduce(lambda x, y: x + y, items)
print(sum_all)
####################################################################################
# Вычисление наибольшего элемента в списке при помощи reduce
print('**********Вычисление наибольшего элемента в списке при помощи reduce********')
from functools import reduce
items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a, b: a if (a > b) else b, items)
print(all_max)
####################################################################################
'''
Программа, которая определяет, на какое максимальное количество одинаковых подстрок 
можно разбить данную строку так, чтобы все элементы строки были задействованы.
'''
# подстроки строки
print('**********Количество подстрок в строке********')
from math import gcd
from functools import reduce
from collections import Counter

line = 'maxmaxmax'

d = Counter(line)
n = reduce(gcd, d.values())

print(n)
####################################################################################