import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
stk = []

for item in enumerate(A):
    index, height = item
    if stk:
        while stk and height > stk[-1][1]:
            current_index, _ = stk.pop()
            answer[current_index] = height

        else:
            stk.append((index, height))
    else:
        stk.append((index, height))

print(*answer)