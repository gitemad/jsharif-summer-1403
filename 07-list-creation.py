# Method #1
# squares = []

# for i in range(1, 11):
#     squares.append(i ** 2)

# print(squares)


# Method #2
# def square(n):
#     return n ** 2

# squares = map(square, range(1, 11))

# print(list(squares))

# Method #3
# squares = [i ** 2 for i in range(1, 11)]
# squares = [pow(i, 2) for i in range(1, 11)]
# print(squares)

# sentence = 'the rocket came back from mars'
# vowels = [ch for ch in sentence if ch in 'aeiou']
# vowels = {ch for ch in sentence if ch in 'aeiou'}
# print(vowels)

# numbers = [1, 5, -4, -2, 7, -9, 6]
# abs_numbers = [n if n >= 0 else -n for n in numbers]

matrix = [[i for i in range(5)] for _ in range(3)]

flat = [num for row in matrix for num in row]
print(flat)

flat = []
for row in matrix:
    for num in row:
        flat.append(num)

print(flat)