"""
На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию


Ответ:
Реализация циклического буфера CycleBufferQueue работает быстрее, чем
CycleBufferList за счет использования deque (двусторонняя очередь) при добавлении новых элементов,
но медленее при их получении.
CycleBufferList менее эффективна по использованию памяти.


"""
from collections import deque


class CycleBufferList:
    def __init__(self):
        self.items = []

    def add(self, x):
        self.items.insert(0, x)

    def get(self):
        return self.items.pop()


class CycleBufferQueue:
    def __init__(self):
        self.items = deque()

    def add(self, item):
        self.items.appendleft(item)

    def get(self):
        return self.items.pop()

# Сравнение скорости заполнения буфера и получения элементов из него 10000 раз:


"""
from timeit import timeit


add_to_queue = timeit('s.appendleft(5)', 'import collections; s = collections.deque([1,2,3,4])', number=10000)
add_to_list = timeit('s.insert(0,5)', 's = [1,2,3,4]', number=10000)
get_from_queue = timeit('collections.deque([1,2,3,4]).pop()', 'import collections', number=10000)
get_from_list = timeit('[1,2,3,4].pop()', number=10000)
print(f"Время добавления элемента в CycleBufferList - {add_to_list} и CycleBufferQueue - {add_to_queue} секунд")
print(f"Время получения элемента и из CycleBufferList - {get_from_list } и CycleBufferQueue - {get_from_queue} секунд")
print(add_to_queue < add_to_list)
print(get_from_queue > get_from_list)
"""