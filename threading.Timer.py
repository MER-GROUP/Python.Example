####################################################################################
'''
Класс Timer() модуля threading в Python.
Создание и запуск потоков-таймеров.

Синтаксис:
import threading
timer = threading.Timer(interval, function, args=None, kwargs=None)

Параметры:
interval - интервал запуска вызываемого объекта (функции),
function - вызываемый объект (функция),
args=None - позиционные аргументы function,
kwargs=None - ключевые аргументы function.

Возвращаемое значение:
объект Timer.

Описание:
Класс Timer() модуля threading создает таймер, который будет запускать функцию function 
с аргументами args и ключевыми аргументами kwargs по прошествии интервала interval секунд.

Если args равен None (по умолчанию), то будет использоваться пустой список. 
Если kwargs равен None (по умолчанию), то будет использоваться пустой словарь.

Этот класс представляет действие, которое следует запускать только по прошествии 
определенного времени - таймер. Таймер является подклассом threading.Thread() и, 
как таковой, также служит примером создания пользовательских потоков.

Таймеры запускаются, как и потоки, путем вызова их метода Timer.start(), 
унаследованного от класса threading.Thread().

Таймер можно остановить до того, как его действие начнется, вызвав метод Timer.cancel(). 
Интервал, который таймер будет ожидать перед выполнением своего действия, 
может не совпадать с интервалом, указанным пользователем.
'''
####################################################################################
# через 30 секунд будет напечатано "hello, world".
from threading import Timer

def hello():
    print("hello, world")

t = Timer(30.0, hello)
t.start()  
####################################################################################
'''
Методы объекта Timer.

Объект Timer дополнительно определяет один метод. 
Остальные методы он наследует от класса threading.Thread().

Timer.cancel():
Метод Timer.cancel() останавливает таймер и отменяет выполнение действия таймера. 
Метод будет работать только в том случае, если таймер все еще находится 
в стадии ожидания. Сработавший таймер остановить нельзя.
'''
####################################################################################
'''
Примеры создания и запуска потоков-таймеров.

Таймер начинает свою работу после задержки и может быть отменен в любой момент 
в течение этого времени задержки.

Второй таймер в этом примере никогда не запускается, а первый таймер запускается 
после того, как остальная часть основной программы завершена.

Так как первый таймер это не поток демона, то он присоединяется неявно, 
когда основной поток завершится, по этому delayed() сообщение не напечатает.
'''
import threading, time

def delayed():
    th_name = threading.current_thread().name
    print(f'Th:{th_name} Worker запущен')

# Создание и запуск потоков таймеров
t1 = threading.Timer(0.3, delayed)
t1.name = 'Timer-1'
t2 = threading.Timer(0.3, delayed)
t2.name = 'Timer-2'

print('Запуск таймеров')
t1.start()
t2.start()

print(f'Ожидание перед завершением {t2.name}')
time.sleep(0.2)
print(f'Завершение {t2.name}')
t2.cancel()
print('Выполнено')

# Запуск таймеров
# Ожидание перед завершением Timer-2
# Завершение Timer-2
# Выполнено
# Th:Timer-1 Worker запущен
####################################################################################