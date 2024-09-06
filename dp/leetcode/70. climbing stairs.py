class Solution(object):
    def climbStairs(self, n):
        memorization = {1: 1, 2: 2}

        if 3 > n:
            return memorization[n]

        for i in range(3, n + 1):
            memorization[i] = memorization[i-1] + memorization[i-2]

        return memorization[n]


solution = Solution()

print(solution.climbStairs(2))
