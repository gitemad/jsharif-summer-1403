# def function_name():
#     print('inside function')

# print("before calling function")
# function_name()
# print("after calling function")

# # Positional arguments (required arguements)
# def print_bill_item(item, cost):
#     print(f'{item}: {cost}$')

# # correct
# print_bill_item('Mobile', 1500)

# # incorrect
# # print_bill_item(1500, 'Mobile')

# # error
# # print_bill_item('Mobile')
# # print_bill_item('Mobile', 1500, 3)


# # Keyword arguments
# def print_bill_item(item, fee, num):
#     print(f'item: {item}\tfee: {fee}$\tcost: {fee * num}$')

# print_bill_item('Cheese', 10, 2)
# print_bill_item(num=2, item='Cheese', fee=10)
# print_bill_item('Cheese', num=2, fee=10)

# # error
# print_bill_item(item='Cheese', 10, 2)


# # default parameters
# def print_bill_item(item, fee, num=1):
#     print(f'item: {item}\tfee: {fee}$\tcost: {fee * num}$')

# print_bill_item('Mobile', 1500)
# print_bill_item('Mobile', 1500, 2)
# print_bill_item('Mobile', 1500, num=3)


# # mutable default parameters
# def f(my_list=[]):
#     my_list.append('###')
#     print(my_list)

# def f2(my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append('###')
#     print(my_list)

# f(my_list=[1, 2, 3])
# f(my_list=['a', 'b', 'c'])
# f()

# f()
# f()

# f2(my_list=[1, 2, 3])
# f2(my_list=['a', 'b', 'c'])
# f2()

# f2()
# f2()


# def f(inner_str):
#     print('inside:', inner_str, id(inner_str))
#     inner_str += 'extra'
#     print('inside:', inner_str, id(inner_str))

# outer_str = 'string'
# print('outside:', outer_str, id(outer_str))
# f(outer_str)
# print('outside:', outer_str, id(outer_str))

# def f(inner_list):
#     print('inside:', inner_list, id(inner_list))
#     inner_list += ['extra']
#     print('inside:', inner_list, id(inner_list))

# outer_list = ['string']
# print('outside:', outer_list, id(outer_list))
# f(outer_list)
# print('outside:', outer_list, id(outer_list))

# def sqrt(n):
#     return n ** 0.5

# def f():
#     return 1, 2, 3

# def avg(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
    
#     return total / len(numbers)

# print(avg(1))
# print(avg(1, 2))
# print(avg(1, 2, 3))
# print(avg(1, 2, 3, 4))

# def f(x, y, z):
#     print('x', x)
#     print('y', y)
#     print('z', z)

# t = ('x', 'y', 'z')
# f(*t)

# def f(**kwargs):
#     for key, val in kwargs.items():
#         print(key, '->', val)

# f(a=1, b=2, c=3)

# def concat(*args, prefix='->'):
#     print(f'{prefix}{".".join(args)}')

# # -> a.b.c
# concat('a', 'b', 'c')

# def repeat(a: int, b: str) -> str:
#     return b * a

# def area(r: {
#     'desc': 'radius of circle',
#     'type': float
# }) -> {
#     'desc': 'area of circle',
#     'type': float
# }:
#     return 3.141592 * (r ** 2)

# print(area.__annotations__)

# def sqrt(n):
#     return n ** 0.5

# sqrt = lambda n: n ** 0.5

students = [
    {
        "name": 'student 1',
        "phone": "09123456789"
    },
    {
        "name": 'student 2',
        "phone": "09123456789"
    },
    {
        "name": 'student 3',
        "phone": "09123456789"
    },
    {
        "name": 'student 4',
        "phone": "09123456789"
    },
]
students_names = list(map(lambda student: student['name'], students))
print(students_names)