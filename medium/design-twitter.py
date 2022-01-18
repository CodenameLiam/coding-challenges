from typing import List
import collections

class Twitter:

    def __init__(self):
        self.follows = collections.defaultdict(set)
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append({"user": userId, "tweet": tweetId})
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(filter(lambda x : x["user"] == userId or x["user"] in self.follows[userId], self.tweets))
        return list(map(lambda x : x["tweet"], feed[:-11:-1]))
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
twitter = Twitter();
# twitter.postTweet(1, 5); 
# twitter.getNewsFeed(1);  
# twitter.follow(1, 2);    
# twitter.postTweet(2, 6); 
# twitter.getNewsFeed(1);  
# twitter.unfollow(1, 2);  
# twitter.getNewsFeed(1);  

twitter.postTweet(1, 4)
twitter.postTweet(2, 5)
twitter.unfollow(1, 2)