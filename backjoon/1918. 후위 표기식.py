import sys
from collections import deque

equation = deque(str(sys.stdin.readline().strip()))
result = ''
symbol = []

while equation:
    eq = equation.popleft()

    if eq == '(':
        symbol.append(eq)
        while eq != ')':
            eq = equation.popleft()
            # A + (B + C * D)
            if eq == ')':
                current_symbol = symbol.pop()
                prev_symbol = symbol.pop()

                while prev_symbol != '(' or current_symbol != '(':
                    if (current_symbol == '*' or current_symbol == '/') and (prev_symbol == '+' or prev_symbol == '-'):
                        result += current_symbol
                        result += prev_symbol

                    elif (prev_symbol == '*' or prev_symbol == '/') and (current_symbol == '+' or current_symbol == '-'):
                        result += prev_symbol
                        result += current_symbol

                    else:
                        result += prev_symbol
                        result += current_symbol

                else:
                    result += current_symbol

            elif eq == '+' or eq == '-' or eq == '*' or eq == '/':
                symbol.append(eq)
            else:
                result += eq
    elif eq == '+' or eq == '-' or eq == '*' or eq == '/':
        symbol.append(eq)
    else:
        result += eq



print(symbol)
print(result)

