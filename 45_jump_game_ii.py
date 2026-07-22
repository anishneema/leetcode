class Solution:
    def jump(self, nums: List[int]) -> int:

        left = 0
        right = 0
        ans = 0
        farthest = 0

        while (farthest < len(nums) -1):


            for i in range(left, right + 1):

                farthest = max(farthest, nums[i] + i)
            
            ans += 1
            left = right
            right = farthest 
        
        return ans