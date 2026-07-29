class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def dp(state):

            if state == n:
                return 1
            if state > n:
                return 0
            
            if state in memo:
                return memo[state]
            
            memo[state] = dp(state+1) + dp(state+2)
            return memo[state]
        
        return dp(0)