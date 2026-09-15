class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0
                

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        user_followers = self.follows[userId]
        user_tweets = self.tweets[userId][-10:]
        followers_tweets = [self.tweets[f][-10:] for f in user_followers]
        followers_tweets_flattened = [item for sublist in followers_tweets for item in sublist] 
        all_tweets = followers_tweets_flattened + user_tweets
        
        heapq.heapify(all_tweets)
        top10 = heapq.nlargest(10, all_tweets)

        return [tweet for time, tweet in top10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
