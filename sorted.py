####################################################################################
# сортировка списка кортежей
print('**********сортировка списка кортежей********')
arr = [('d', 3), ('x', 2), ('a', 2)]
print(arr)
print(sorted(arr))
print(sorted(arr, key=lambda x: (x[1], x[0])))
print(sorted(arr, key=lambda x: (x[1], x[0]), reverse=True))
print(sorted(arr, key=lambda x: (-x[1], x[0]), reverse=True))
print(sorted(arr, key=lambda x: (-x[1], x[0])))
####################################################################################