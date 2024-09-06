cost = [10, 15, 20, 17, 1]
memo = {0: 0, 1: 1}

def dp(n):
    for i in range(2, n + 1):
        memo[i] = min((memo[i-2] + cost[i-2]), (memo[i-1] + cost[i-1]))

    return memo[n]

print(dp(5))

