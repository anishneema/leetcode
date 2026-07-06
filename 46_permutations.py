class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr):

            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for j in range(len(nums)):
                if nums[j] not in curr:
                    curr.append(nums[j])
                    backtrack(curr)
                    curr.pop()
            
        
        ans = []
        backtrack([])
        return ans