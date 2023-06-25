"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
s_1 = b'attribute'
s_2 = b'класс'
s_3 = b'функция'
s_4 = 'type'
# "C:\Users\alibe\Desktop\drf\drf\асинхронный чат\Scripts\python.exe" "C:/Users/alibe/Desktop/асинхронный чат/asynchronous_chat/task_3.py"
#   File "C:\Users\alibe\Desktop\асинхронный чат\asynchronous_chat\task_3.py", line 13
#     s_2 = b'класс'
#                        ^
# SyntaxError: bytes can only contain ASCII literal characters
#
# Process finished with exit code 1
