from sys import stdin

N = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
stk = []
answers = ['0'] * N

for i in range(N-1, -1, -1):
    while stk and towers[i] >= stk[-1][1]:
        answers[stk.pop()[0]] = str(i+1)
    stk.append((i, towers[i]))

print(" ".join(answers))