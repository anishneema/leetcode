class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr, i):

            for i in range(i, len(nums)):

                curr.append(nums[i])
                ans.append(curr[:])
                backtrack(curr, i+1)
                curr.pop()
        
        ans = [[]]
        backtrack([], 0)
        return ans