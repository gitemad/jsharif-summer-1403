# def say_hello(name):
#     return f'Hello {name}'

# def say_hi(name):
#     return f'Hi {name}'

# def greet(greeter_func, name):
#     return greeter_func(name)

# print(greet(say_hello, 'Emad'))

# def parent():

#     print('parent')

#     def first_child():
#         print('first_child')

#     def second_child():
#         print('second_child')
    
#     second_child()
#     first_child()

# parent()



# def parent(num):
#     def first_child():
#         print('first_child')

#     def second_child():
#         print('second_child')
    
#     if num == 1:
#         return first_child
#     else:
#         return second_child

# parent(2)()

# def my_decorator(func):
#     def wrapper():
#         print('before calling func')
#         func()
#         print('after calling func')
    
#     return wrapper

# @my_decorator
# def say_hi():
#     print('Hi!')

# def say_hello():
#     print('Hello!')

# # say_hi = my_decorator(say_hi)

# say_hi()


# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
    
#     return wrapper_do_twice

# @do_twice
# def greet(name):
#     print(f'Hello {name}')


# def repeat(num_times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(num_times=4)
# def greet(name):
#     print(f'Hello {name}')

# greet('Emad')


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        output = func(*args, **kwargs)

        return output
    
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f'Creating greet function')
    return f'Hi {name}'

output = greet('Ali')

print(output)
