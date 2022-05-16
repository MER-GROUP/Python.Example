####################################################################################
# поиск одинаковых букв в слове с помощью словаря dict()
print('**********поиск одинаковых букв в слове с помощью словаря dict()********')
my_dict = dict()
word = 'maximum'
for i in word:
    my_dict[i] = my_dict.get(i, 0) + 1
print(my_dict)
####################################################################################
# поиск одинаковых букв в слове с помощью словаря collections.Counter
print('**********поиск одинаковых букв в слове с помощью словаря collections.Counter********')
my_dict = dict()
word = 'maximum'
import collections
my_dict = collections.Counter(word)
print(my_dict)
print(dict(my_dict))
####################################################################################
'''
Dict subclass for counting hashable items. Sometimes called a bag or multiset. 
Elements are stored as dictionary keys and their counts are stored as dictionary values.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string
>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15
>>> c['a']                          # count of letter 'a'
5
>>> for elem in 'shazam':           # update counts from an iterable
...     c[elem] += 1                # by adding 1 to each element's count
>>> c['a']                          # now there are seven 'a'
7
>>> del c['b']                      # remove all 'b'
>>> c['b']                          # now there are zero 'b'
0
>>> d = Counter('simsalabim')       # make another counter
>>> c.update(d)                     # add in the second counter
>>> c['a']                          # now there are nine 'a'
9
>>> c.clear()                       # empty the counter
>>> c
Counter()
Note: If a count is set to zero or reduced to zero, 
it will remain in the counter until the entry is deleted or the counter is cleared:

>>> c = Counter('aaabbc')
>>> c['b'] -= 2                     # reduce the count of 'b' by two
>>> c.most_common()                 # 'b' is still in, but its count is zero
[('a', 3), ('c', 1), ('b', 0)]
'''
####################################################################################