from functools import reduce


def evaluate(coefficients, x):
    return reduce(lambda a, b: int(a) * x + int(b), coefficients.split())


print(evaluate(input(), int(input())))
