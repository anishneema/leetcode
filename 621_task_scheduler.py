class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        queue = deque()
        freq = Counter(tasks)
        minheap = [-value for value in freq.values()]
        heapq.heapify(minheap)
        time = 0


        while minheap or queue:

            time +=1 

            if queue and queue[0][1] == time:
                v = queue.popleft()
                heapq.heappush(minheap, v[0])

            if minheap:

                v = heapq.heappop(minheap)
                v+=1
                if v:
                    queue.append((v,time+n+1))
            

        return time