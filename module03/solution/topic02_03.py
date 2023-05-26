import math
import topic02_03_token

# Task 1
x1, x2, y1, y2 = float(input()), float(input()), float(input()), float(input())
print(math.hypot(x1 - y1, x2 - y2))

# Task 2
expression = input("Введите математическое выражение: ")
tokens = topic02_03_token.tokenize_expression(expression)
print("Список лексем:", tokens)