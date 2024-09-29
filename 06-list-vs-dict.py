import time
lst = [i for i in range(10_000_000)]

dct = {i: i for i in range(10_000_000)}

start = time.perf_counter()
print(9_999_999 in lst)
end = time.perf_counter()

print('list:', end - start)

start = time.perf_counter()
print(9_999_999 in dct)
end = time.perf_counter()

print('dict:', end - start)