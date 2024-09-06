import sys

N = int(sys.stdin.readline().rstrip())

top_down_memo = {1: 0}


def top_down(n):
    if n in top_down_memo.keys():
        return top_down_memo[n]
    if (n % 3 == 0) and (n % 2 == 0):
        top_down_memo[n] = min(top_down(n // 3) + 1, top_down(n // 2) + 1)
    elif n % 3 == 0:
        top_down_memo[n] = min(top_down(n // 3) + 1, top_down(n - 1) + 1)
    elif n % 2 == 0:
        top_down_memo[n] = min(top_down(n // 2) + 1, top_down(n - 1) + 1)
    else:
        top_down_memo[n] = top_down(n - 1) + 1
    return top_down_memo[n]


# print(top_down(N))


bottom_up_memo = [0] * (N + 1)

for i in range(2, N + 1):
    bottom_up_memo[i] = bottom_up_memo[i - 1] + 1

    if i % 2 == 0:
        bottom_up_memo[i] = min(bottom_up_memo[i], bottom_up_memo[i // 2] + 1)

    if i % 3 == 0:
        bottom_up_memo[i] = min(bottom_up_memo[i], bottom_up_memo[i // 3] + 1)

print(bottom_up_memo[N])