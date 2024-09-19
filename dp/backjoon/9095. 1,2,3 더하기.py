import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    memo = [0] * (N + 1)

    for i in range(1, N+1):
        if i == 1:
            memo[i] = 1
        elif i == 2:
            memo[i] = 2
        elif i == 3:
            memo[i] = 4
        else:
            memo[i] = memo[i-3] + memo[i-2] + memo[i-1]

    print(memo[N])