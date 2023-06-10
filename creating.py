#Нужно написать две программы: Первая создает бинарный файл (min 2Гб),
# состоящий из случайных 32-разрядных беззнаковых целых чисел (big endian).
# Вторая считает сумму этих чисел (с применением длинной арифметики), находит минимальное и максимальное число.

#Реализуйте две версии -
# 1. Простое последовательное чтение
# 2. Многопоточная + memory-mapped files. Сравните время работы.


from random import randint
from tqdm import tqdm

# Создаём бинарный файл
file_handler = open("endian.bin", "wb")

ves=2*1024*1024*1024/4

for i in tqdm(range(int(ves)+1)):
    file_handler.write(int(randint(0,2**32-1)).to_bytes(4, "big"))

file_handler.close()