import sys

syntax = list(str(sys.stdin.readline().strip()))
M = int(sys.stdin.readline())
stk = []

for _ in range(M):
    command = list(sys.stdin.readline().strip())

    if command[0] == 'L':
        if len(syntax) > 0:
            stk.append(syntax.pop())

    elif command[0] == 'D':
        if len(stk) > 0:
            syntax.append(stk.pop())

    elif command[0] == 'B':
        if len(syntax) > 0:
            syntax.pop()

    else:
        print(command)
        syntax.append(command[2])


syntax.extend(reversed(stk))

print(''.join(syntax))