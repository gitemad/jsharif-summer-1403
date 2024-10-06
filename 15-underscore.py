# from my_module import *
# import my_module

# my_module._internal_func()

# # single trailing underscore
# def make_object(name, class_):
#     pass

# class Test:
#     def __init__(self):
#         self.a = 1
#         self._b = 2
#         self.__c = 3

# class ExtendedTest(Test):
#     def __init__(self):
#         super().__init__()
#         self.a = 'overridden'
#         self._b = 'overridden'
#         self.__c = 'overridden'

# class MangledMethod:
#     def __method(self):
#         return 'mangled method'
    
#     def call_it(self):
#         return self.__method()

# m = MangledMethod()
# print(m.call_it())

# class PrefixPostfixTest:
#     def __init__(self):
#         self.__num__ = 42

# print(PrefixPostfixTest().__num__)

for _ in range(5):
    print('aaaa')

name, creator, _, _ = ('Python', 'Guido Van Rossum', 1991, 'OOP')

3_000_000_000