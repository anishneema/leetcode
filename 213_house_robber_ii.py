class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        
        def house_rob(houses):
            
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            arr = [0] * len(houses)
            arr[0] = houses[0]
            arr[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):

                arr[i] = max(houses[i] + arr[i-2], arr[i-1])
            
            return arr[len(houses) - 1]
        
        return max(house_rob(nums[1:]), house_rob(nums[:-1]))