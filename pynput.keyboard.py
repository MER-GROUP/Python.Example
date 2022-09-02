####################################################################################
'''
Использование модуля pynput.keyboard библиотеки pynput в Python.
Модуль pynput.keyboard библиотеки pynput содержит классы для управления и мониторинга клавиатуры.
'''
####################################################################################
'''
Управление клавиатурой.
Для управления клавиатурой используйте класс keyboard.Controller следующим образом:
'''
print('--------pynput.keyboard import Key, Controller---------')
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Нажимает и отпускает клавишу пробела
print('-1----------------')
keyboard.press(Key.space)
keyboard.release(Key.space)
print('\n-1----------------')

# печатает строчную букву `a`, будет работать, даже если ни 
# одна клавиша на физической клавиатуре не помечена буквой `a`.
print('-2----------------')
keyboard.press('a')
keyboard.release('a')
print('\n-2----------------')

# печатает две заглавные буквы `A`:
# выводим сразу заглавную 'A'
print('-3----------------')
keyboard.press('A')
keyboard.release('A')
# выводим заглавную 'A' через нажатие `Key.shift`
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')
print('\n-3----------------')

# печатает 'Hello World', используя метод быстрого ввода
print('-4----------------')
keyboard.type('Hello World')
print('\n-4----------------')

# вывод
'''
red@red:~/WORK/PYTHON/MyPROG/Python.Example$ python pynput.keyboard.py
-1----------------

-1----------------
-2----------------
 a
-2----------------
-3----------------
AA
-3----------------
-4----------------
Hello World
-4----------------
red@red:~/WORK/PYTHON/MyPROG/Python.Example$ aAAHello World
'''
####################################################################################
'''
Мониторинг клавиатуры.
Для мониторинга клавиатуры используйте класс keyboard.Listener следующим образом:
'''
print('--------from pynput import keyboard---------')
from pynput import keyboard

def on_press(key):
    try:
        print(f'Нажата буквенно-цифровая клавиша: {key.char}')
    except AttributeError:
        print(f'Нажата специальная клавиша: {key}')

def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.esc:
        # Возврат False - остановит слушатель
        return False

# блок `with` слушает события до выхода 
# до остановки слушателя
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
        ) as listener:
    listener.join()

# #...или неблокирующим способом:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release
# )
# listener.start()
'''
Слушатель клавиатуры keyboard.Listener - это threading.Thread, 
и все обратные вызовы будут вызываться из потока.

Чтобы остановить слушатель клавиатуры, можно вызвать keyboard.Listener.stop() 
из любого места, что в свою очередь вызовет исключение StopException 
или возвратить False из функции обратного вызова.

Аргумент key, который передается слушателем в обратные вызовы, является keyboard.Key 
для специальных клавиш и keyboard.KeyCode для обычных буквенно-цифровых клавиш 
или просто None для неизвестных клавиш.

При использовании приведенной выше неблокирующей версии текущий поток продолжит 
выполнение. Это может быть необходимо при интеграции с другими платформами 
графического интерфейса, включающими основной цикл, но при запуске из скрипта 
это приведет к немедленному завершению программы.
'''
####################################################################################

####################################################################################