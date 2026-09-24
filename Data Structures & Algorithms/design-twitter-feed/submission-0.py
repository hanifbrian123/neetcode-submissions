class Twitter:
    def __init__(self):
        self.curTime = 0
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.curTime+=1
        if userId in self.users:
            self.users[userId]['tweets'].append((self.curTime, tweetId))
        else:
            self.users[userId] = {
                "tweets": [(self.curTime, tweetId)],
                "followees": set()
            }

    def getNewsFeed(self, userId: int) -> List[int]:
        # userId => curProgres tweet most recent
        peopleToShow_to_CurProgres = {
            followeeId: len(self.users[followeeId]['tweets']) - 1
            for followeeId in self.users[userId]['followees']
        }
        peopleToShow_to_CurProgres[userId] = len(self.users[userId]['tweets']) - 1
        
        ### DEBUG START
        # for x in self.users:
        #     print(f"{x} => {self.users[x]}")
        # print(peopleToShow_to_CurProgres)
            

        ### DEBUG END



        # get 10 most recent
        res = []
        for i in range(10):
            bestTime = 0
            bestUserId = None
            bestTweetId = None
            for usrId in peopleToShow_to_CurProgres:
                if peopleToShow_to_CurProgres[usrId] < 0:
                    continue
                time, tweetId = self.users[usrId]['tweets'][peopleToShow_to_CurProgres[usrId]]
                if time > bestTime:
                    bestTime = time
                    bestUserId = usrId
                    bestTweetId = tweetId
            if bestUserId:
                res.append(bestTweetId)
                peopleToShow_to_CurProgres[bestUserId] -= 1
            else:
                break
        return res

        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users: 
            self.users[followerId] = {
                "tweets": [],
                "followees": set()
            }
        if followeeId not in self.users: 
            self.users[followeeId] = {
                "tweets": [],
                "followees": set()
            }
        self.users[followerId]['followees'].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users: 
            self.users[followerId] = {
                "tweets": [],
                "followees": set()
            }
            return
        if followeeId not in self.users: 
            self.users[followeeId] = {
                "tweets": [],
                "followees": set()
            }
            return
        self.users[followerId]['followees'].remove(followeeId)

# => m (get all tweets themself and them followee)
# => heapfiy(m) => m 
# => 10 * n
# 10 * n
# n log n

# m + m + log m
# 10^4 + 10^4 + 10
# 20^4 + 10 =~ 20^4



# user: {followers}
# user: {tweet}

# time complexity: n * (m log m) => 4+4+1 => O(n) => 10^9 > 10^8
# n * m

# n * 10^3 => 10^7

# tweet: heapq [(-timeid, tweetId, userId)] => (m log m) => num of tweet is m

# users: {
#     "1": {
#         "follow": set(userId),
#         "tweet": heapq()
#     }
# }



# for f in followee => n * 10

# get news feed:
# iterate followes => maximum value from heap[0] each iterate
# 10 * (n + log(n)) => 500*10 => 5000 => 10^3




# ###
# get news feed 
# => heappop the tweet until tweet is empty or got 10 tweet already. if tweet.userId in this.user.followers or user.id == tweet.userId
# => add the remove before again to the heap
# => m log m

# post tweet
# => get heap.peek[0] -> (+1) -> min it for timeid -> insert into heapq (timeid, tweetid, userId)
# => log m

# follow
# => user.follow.add(userid)
# => constraint: userid != this.userid


# unfollow: user.follow.remove