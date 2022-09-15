# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 
# Example 1:
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


# using defaultdict, don't need to initialize hashmaps or sets, saves few lines of code
# hashmap, hashset--- adds and removes in O(1)

from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # hashmap--  list of [count, tweetID]
        self.followMap = defaultdict(set)  # hashset--  set of followeeID
        

    def postTweet(self, userId: int, tweetId: int) -> None:     # O(1)
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1   # since we are creating minheap

        
    def getNewsFeed(self, userId: int) -> List[int]:
        # Complexity: O(k) ~ O(k + 10.logk)  # k is the number of followee (k number of tweet lists) for the user, finding minimum logk (among last values from k lists), do it 10 times     
        # heap push k.logk, heapify O(k)
        res = []  # ordered starting from recent
        minHeap = []
        
        self.followMap[userId].add(userId)        # a user follows himself
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])    #index-1 since we are going to go to back to list self.tweetMap[followeeId] and get the next position at the prev index, that is the next position we are going to look at in the list
        heapq.heapify(minHeap)
        
        while minHeap and len(res)<10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            if index>=0:  # if there is more tweets more the same followee
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res                

    def follow(self, followerId: int, followeeId: int) -> None:   # O(1)
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:   # O(1)
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)