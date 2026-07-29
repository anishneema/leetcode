class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        value = [0] * len(nums)

        value[0] = nums[0]
        value[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):

            value[i] = max(value[i-1], value[i-2] + nums[i])
        

        return value[len(nums) -  1]