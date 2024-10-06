# file = open('hello.txt', 'w')

# try:
#     file.write('Hello, World!')
# finally:
#     file.close()

# with open('hello.txt', mode='w') as file:
#     file.write('Hello, World!')

# class WritableFile:
#     def __init__(self, file_path):
#         self.file_path = file_path
    
#     def __enter__(self):
#         self.file_obj = open(self.file_path, mode='w')
#         return self.file_obj

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file_obj:
#             self.file_obj.close()

# with WritableFile('hello.txt') as file:
#     file.write('Hello from custom context manager')

from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode='w')
    try:
        yield file
    finally:
        file.close()


with writable_file('hello.txt') as file:
    file.write('Hello from decorated context manager')