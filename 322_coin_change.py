class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        
        def dp(amount):

            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            if amount < 0:
                return float('inf')
            
            best = float('inf')
            
            for c in coins:

                candidate = dp(amount - c) + 1
                best = min(candidate, best)
            
            memo[amount] = best
            return best

        result = dp(amount)

        return result if result != float('inf') else -1