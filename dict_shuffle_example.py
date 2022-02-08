####################################################################################
#перемешивание ключей в словаре
import random
d = {1:2, 3:4, 5:6, 7:8, 9:10}
print(d)
#{1: 2, 3: 4, 9: 10, 5: 6, 7: 8}

keys =  list(d.keys())      # Python 3; use keys = d.keys() in Python 2
random.shuffle(keys)
print([(key, d[key]) for key in keys])
#[(1, 2), (5, 6), (7, 8), (9, 10), (3, 4)]

random.shuffle(keys)
print([(key, d[key]) for key in keys])
#[(9, 10), (3, 4), (1, 2), (7, 8), (5, 6)]

random.shuffle(keys)
print([(key, d[key]) for key in keys])
#[(1, 2), (7, 8), (3, 4), (5, 6), (9, 10)]
####################################################################################