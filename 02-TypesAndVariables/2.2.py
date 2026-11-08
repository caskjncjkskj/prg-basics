expressions = [
    ("3 * 2 + 1", 2, 3, 3 * 2 + 1),
    ("5 + 10 * 5", 2, 3, 5 + 10 * 5),
    ("4 + 4 / 2 ** 2", 3, 4, 4 + 4 / 2 ** 2),
    ("4 % 3 % 2 % 1", 3, 4, 4 % 3 % 2 % 1),
    ("1 + 2 % 3 ** 4 * 5", 4, 5, 1 + 2 % 3 ** 4 * 5),
    ("True != False", 1, 2, True != False),
]
for expression, operators, arguments, value in expressions:
    print(f"{expression}: {operators} operators, {arguments} arguments, value = {value}")
