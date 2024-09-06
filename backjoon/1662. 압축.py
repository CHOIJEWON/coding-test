import sys

S = list(str(sys.stdin.readline().strip()))
symbol = []
answer = 0
temp = 0
bracket_point = 0
while S:
    string = S.pop()

    if string == ')':
        symbol.append(string)
        temp += bracket_point
        bracket_point = 0
    elif string == '(':
        symbol.pop()
        operator = int(S.pop())
        temp += bracket_point
        temp *= operator
        bracket_point = 0
    else:
        if symbol and string != '0':
            bracket_point += 1
        else:
            if string != '0':
                answer += 1

answer += temp

print(answer)