# print(0 / 0)

# age = int(input("Enter your age: "))

# if age < 0:
#     raise Exception(f'Age must be positive. The value of age was: {age}')

# num = int(input('Enter numerator: '))
# den = int(input('Enter denominator: '))

# try:
#     print(num / den)
# except ZeroDivisionError:
#     print('Denominator must not be zero.')

# print('Program continues ...')

# num = 2
# den = 0

# dictionary = {
#     'name': 'Emad'
# }

# l = [1, 2, 3]

# try:
#     print(dictionary['age'])
#     print(l[5])
#     print(num / den)
# except ZeroDivisionError:
#     print('Denominator must not be zero.')
# except (KeyError, IndexError) as e:
#     print(e)


# l = [1, 2, 3]

# try:
#     print(l[5])
# except Exception as e:
#     print(e)

# l = [1, 2, 3]
# try:
#     print(l[5])
# except Exception as e:
#     print(e)
# else:
#     print('execting the else clause')


# l = [1, 2, 3]

# try:
#     print(l[0])
# except Exception as e:
#     print(e)
# finally:
#     print('Executing finally')


# class CustomError(Exception):
#     pass

# raise CustomError('sddsd')


class AgeNotInRange(Exception):

    def __init__(self, age, message='Age not in range'):
        self.age = age
        self.message = message
        super().__init__(self.message)

age = int(input('Enter your age: '))

if not 18 <= age <= 30:
    raise AgeNotInRange(age)