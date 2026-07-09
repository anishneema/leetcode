class Twitter:

    def __init__(self):

        self.feedsmap = defaultdict(list)
        self.followermap = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time+=1
        
        self.feedsmap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        
        candidates = [userId]
        candidates.extend(self.followermap[userId])
        minheap = []

        for user in candidates:

            for tweet in self.feedsmap[user]:

                heapq.heappush(minheap, tweet)

                if len(minheap) > 10:
                    heapq.heappop(minheap)
        
        result = []

        while minheap:

            time, value = heapq.heappop(minheap)

            result.append(value)
        
        return result[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:

        if not (followerId == followeeId):
            self.followermap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.followermap[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)