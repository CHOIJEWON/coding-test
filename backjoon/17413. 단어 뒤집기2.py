import sys

syntax = list(sys.stdin.readline().strip())

stk = []
answer = []
result = ''

while syntax: # syntax가 모두 소진될때 까지™
    word = syntax.pop()

    if word == ' ':
        if stk:
            join_string = ''.join(stk)
            answer.append(join_string)
            stk.clear()
        answer.append(word)

    elif word == '>':
        if stk:
            join_string = ''.join(stk)
            answer.append(join_string)
            stk.clear()

        while syntax:
            stk.append(word)
            word = syntax.pop()
            if word == '<':
                stk.append('<')
                break

        result = ''.join(stk[::-1])
        answer.append(result)
        stk.clear()
    else:
        stk.append(word)

if stk:
    print(''.join(stk) + ''.join(answer[::-1]))
else:
    print(''.join(answer[::-1]))


