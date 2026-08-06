class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summation = sum(nums)

        if summation % 2 != 0:
            return False
        
        target = summation // 2

        memo = {}

        def dp(i, total):

            if (i, total) in memo:
                return memo[(i, total)]

            if nums[i] + total == target:
                memo[(i,total)] = True
                return True
            
            if i == len(nums) - 1:
                memo[(i, total)] = False
                return False
            

            if i < len(nums) - 1:

                if total + nums[i] > target:
                    result = dp(i+1, total)
                else:
                    result = dp(i+1, total + nums[i]) or dp(i+1, total)
            
            memo[(i,total)] = result
            return result
        
        
        return dp(0,0)