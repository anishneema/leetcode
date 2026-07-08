class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            newstone = stone1 - stone2

            heapq.heappush(stones, newstone)
        
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]