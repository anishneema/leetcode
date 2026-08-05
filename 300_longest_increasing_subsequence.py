class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        best = 1

        def dp(i):
            

            if i == len(nums) - 1:
                memo[i] = 1
                return memo[i]
            
            if i in memo:
                return memo[i]
            
            for j in range(i+1, len(nums)):

                if nums[i] < nums[j]:
                    result = 1 + dp(j)
                    if i in memo:
                        memo[i] = max(memo[i], result)
                    else:
                        memo[i] = result
            
            if i not in memo:
                memo[i] = 1
            
            return memo[i]
        
        for i in range(len(nums)):

            best = max(best, dp(i))
        
        return best