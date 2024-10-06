import multiprocessing
import time

# def recur_fibo(n):
#     if n <= 1:
#         return n
    
#     return recur_fibo(n - 1) + recur_fibo(n - 2)

# def print_fibo_sequences(n):
#     for i in range(n + 1):
#         print(recur_fibo(i))


# # if __name__ == '__main__':
# #     t0 = time.perf_counter()

# #     for i in range(8):
# #         print_fibo_sequences(30)

# #     t1 = time.perf_counter()

# #     print(t1 - t0)

# if __name__ == '__main__':
#     t0 = time.perf_counter()
#     processes = []

#     for i in range(8):
#         p = multiprocessing.Process(target=print_fibo_sequences, args=(30,))
#         processes.append(p)
    
#     for p in processes:
#         p.start()
    
    
#     for p in processes:
#         p.join()

#     t1 = time.perf_counter()

#     print(t1 - t0)


def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    shared_value = multiprocessing.Value('i', 0)
    print(f'Value at beginning: {shared_value.value}')

    p1 = multiprocessing.Process(target=add_100, args=(shared_value, lock))
    p2 = multiprocessing.Process(target=add_100, args=(shared_value, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Value at end: {shared_value.value}')