# 2. Многопоточная + memory-mapped files. Сравните время работы.
import time
import mmap
import threading

ves = 2*1024*1024*1024/4

num_of_treads=4
num_per_thread=int(ves/num_of_treads)

def thread_job(mobj, start, end, summ, number,maxx,minn):
    for i in range(start, end):
        n= int.from_bytes(mobj[i*4:i*4+4], 'big')
        maxx[number]=max(maxx[number],n)
        minn[number]=min(minn[number],n)
        summ[number] += n




def run_threads(count, mobj, num_per_thread):
    maxx=[-1]*count
    minn=[2**32]*count
    summ = [0] * count
    threads = [
        threading.Thread(target=thread_job, args=(mobj, num_per_thread*i, num_per_thread*(i+1), summ, i,maxx,minn))
        for i in range(0, count)
    ]
    for thread in threads:
        thread.start()  # каждый поток должен быть запущен

    for thread in threads:
        thread.join()  # дожидаемся исполнения всех потоков
    min_one=min(minn)
    max_one=max(maxx)
    sum_num = 0
    for i in summ:
        sum_num += i
    all_l={'Min':min_one, 'Max': max_one, 'Sum':sum_num}
    return all_l


start = time.time()

with open("endian.bin", mode="rb") as file_handler:
    with mmap.mmap(file_handler.fileno(), length=0, access=mmap.ACCESS_READ) as mobj:
        all_l = run_threads(num_of_treads, mobj, num_per_thread)

end = time.time() - start

print(all_l)
print(end) ## вывод времени

file_handler.close()
