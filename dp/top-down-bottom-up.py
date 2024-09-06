memo = {}

def top_down(n):
    if n == 1 or n == 2:
        return 1

    if n not in memo:
        memo[n] = top_down(n - 1) + top_down(n - 2)
    return memo[n]


memo2 = {1: 1, 2: 1}

def bottom_up(n):
    if n == 1 or n == 2:
        return 1

    for i in range(3, n + 1):
        memo2[i] = memo2[i-1] + memo2[i-2]

    return memo2[n]


print(bottom_up(6))