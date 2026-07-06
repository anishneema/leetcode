class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):

            for j in range(i, len(nums)):

                if j > i and nums[j] == nums[j-1]:
                    continue
                
                curr.append(nums[j])
                ans.append(curr[:])
                backtrack(curr, j+1)
                curr.pop()
            
        nums.sort()
        ans = [[]]
        backtrack([], 0)
        return ans