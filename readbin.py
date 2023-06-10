
#Реализуйте две версии -
# 1. Простое последовательное чтение


from tqdm import tqdm
import time

ves = 2*1024*1024*1024/4

start = time.time()

file_handler = open("endian.bin", "rb")

maxx=-1
minn=2**32
summ=0
for i in range(int(ves)):
    n=int.from_bytes(file_handler.read(4),'big')
    maxx=max(maxx,n)
    summ+=n
    minn=min(n,minn)
end = time.time() - start

print(summ)
print(end) ## вывод времени

file_handler.close()
