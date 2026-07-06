class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr, pick):

            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for j in range(len(nums)):
                if not pick[j]:
                    curr.append(nums[j])
                    pick[j] = True
                    backtrack(curr, pick)
                    curr.pop()
                    pick[j] = False
            
        
        ans = []
        backtrack([], [False]*len(nums))
        return ans