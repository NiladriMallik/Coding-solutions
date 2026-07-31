class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

###############################################################

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        else:
            return climbStairs(n-1) + climbStairs(n-2)

###############################################################

class Solution:
    def climbStairs(self, n: int) -> int:
        lookup = {}

        def climb(n):
            if n <= 2:
                return n
                
            if n in lookup:
                return lookup[n]

            else:
                lookup[n] = climb(n-1) + climb(n-2)
                return lookup[n]

        return climb(n)