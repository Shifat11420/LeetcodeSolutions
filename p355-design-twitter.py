#https://leetcode.com/problems/design-twitter/


# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

class Twitter:

    def __init__(self):
        self.userDict = {}
        self.tweetDict = {}
        self.tweetcount = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        try:
            x = self.userDict[userId]
        except KeyError:
            self.userDict[userId] = []
            
        try:
            x = self.tweetDict[userId]
        except KeyError:
            self.tweetDict[userId] = []
            
        self.tweetDict[userId].append({self.tweetcount: tweetId})
        self.tweetcount += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        try:
            x = self.userDict[userId]
        except KeyError:
            self.userDict[userId] = []
            
        try:
            x = self.tweetDict[userId]
        except KeyError:
            self.tweetDict[userId] = []
            
        da = {}    
        for followers in self.userDict[userId]:
            if followers in self.userDict[userId]:
                for f in self.tweetDict[followers]:
                    da.update(f)
                    
        for i in self.tweetDict[userId]:
            da.update(i)
        
        sortedkeys = sorted(da.keys(),reverse = True)
        sortedkeys = sortedkeys[:10]
        
        ans =[]
        for i in sortedkeys:
            ans.append(da[i])
        return ans
    

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userDict:
            pass
        else:
            self.userDict[followerId] = []
            
        if followeeId in self.userDict:
            pass
        else:
            self.userDict[followeeId] = []
            
        self.userDict[followerId].append(followeeId)
        
        if followerId in self.tweetDict:
            pass
        else:
            self.tweetDict[followerId] = []
        if followeeId in self.tweetDict:
            pass
        else:
            self.tweetDict[followeeId] = []    
            
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userDict[followerId]:
            count = 0
            cnd = False
            for i in range(len(self.userDict[followerId])):
                if self.userDict[followerId][i] == followeeId:
                    count = i
                    cnd = True
            if cnd == True:
                del self.userDict[followerId][count]



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)