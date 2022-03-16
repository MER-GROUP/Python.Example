####################################################################################
'''
MAC-адрес, также известный как физический адрес, 
является уникальным идентификатором, который 
назначается сетевой карте сетевого адаптера компьютера. 
NIC помогает в соединении компьютера с другими 
компьютерами в сети. MAC-адрес является уникальным 
для всех сетевых карт.
'''
####################################################################################
# Программа Python для вычисления
# MAC-адрес хоста
# используя модуль UUID (uuid – универсальные уникальные идентификаторы)
# getnode() - извлечение MAC-адреса компьютера (устройства)
from uuid import getnode
print('**********Способ 1: использование uuid.getnode ()**********')
# печать значения уникального MAC
# адрес с использованием функций uuid и getnode ()
# вывод не в отформатированном виде
print(getnode())
# вывод не в отформатированном шестнадцатеричном виде
print(hex(getnode()))
####################################################################################
print('**********Способ 2: использование getnode () + format ()**********')
print('----------[для лучшего форматирования]----------')
# Python 3 код для печати MAC
# в отформатированном виде
# соединяет элементы getnode () после каждых 2 цифр
print ("The MAC address in formatted way is : ", end="")
print (':'.join(['{:02x}'.format((getnode() >> ele) & 0xff) for ele in range(0, 8*6, 8)][::-1]))
####################################################################################
print('**********Способ 3: использование getnode () + findall () + re ()**********')
print('----------[для уменьшения сложности]----------')
# Python 3 код для печати MAC
# отформатировано и проще понять
# модуль re - регулярные выражения
# findall() - находит все совпадения
from re import findall
# соединяет элементы getnode () после каждых 2 цифр
# используя регулярное выражение
print ("The MAC address in formatted and less complex way is : ", end="")
print (':'.join(findall('..', '%012x' % getnode())))
####################################################################################