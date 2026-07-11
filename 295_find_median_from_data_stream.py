class MedianFinder:

    def __init__(self):

        self.minheap = []
        self.maxheap = []


        

    def addNum(self, num: int) -> None:

        if len(self.minheap) == 0 or num > self.minheap[0]:
            
            heapq.heappush(self.minheap, num)
        else:
            
            heapq.heappush(self.maxheap, -num)
        

        if len(self.minheap) > len(self.maxheap) + 1:

            heapq.heappush(self.maxheap, -(heapq.heappop(self.minheap)))
        
        if len(self.maxheap) > len(self.minheap):
            
            heapq.heappush(self.minheap, -(heapq.heappop(self.maxheap)))
        

    def findMedian(self) -> float:

        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:

            return (self.minheap[0] - self.maxheap[0]) / 2.0
        
        return self.minheap[0]