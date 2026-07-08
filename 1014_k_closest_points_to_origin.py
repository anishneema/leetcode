class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        maxheap = []
        ans = []
        for i in range(len(points)):

            p1,p2 = points[i]
            distance = -(p1**2 + p2**2)
            heapq.heappush(maxheap, (distance, (p1,p2)))

            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        while maxheap:

            key = heapq.heappop(maxheap)
            ans.append(key[1])
        

        return ans