# class Counter:

#     def __init__(self, max=0):
#         self.max = max
    
#     def __iter__(self):
#         self.n = 0
#         return self
    
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1

#             return result
#         else:
#             raise StopIteration

# for i in Counter(5):
#     print(i)


class InfOddIter:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        num = self.num
        self.num += 2

        return num

odds = iter(InfOddIter())
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))
print(next(odds))