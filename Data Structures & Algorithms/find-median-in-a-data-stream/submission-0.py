class MedianFinder:

    def __init__(self):
        self.upHeap = [] # min heap
        self.downHeap = [] # max heap
        
    def addNum(self, num: int) -> None:
        if self.upHeap and self.downHeap:
            if num >= self.upHeap[0]:
                heapq.heappush(self.upHeap, num)
            else:
                heapq.heappush(self.downHeap, num)
        elif not self.upHeap and not self.downHeap:
            heapq.heappush(self.upHeap, num)
        else:
            if self.upHeap:
                if num >= self.upHeap[0]:
                    heapq.heappush(self.upHeap, num)
                else:
                    heapq.heappush(self.downHeap, -num)
            else:
                if -num >= self.downHeap[0]:
                    heapq.heappush(self.downHeap, -num)
                else:
                    heapq.heappush(self.upHeap, num)
        if abs(len(self.upHeap) - len(self.downHeap)) > 1:
            if len(self.upHeap) > len(self.downHeap):
                temp = heapq.heappop(self.upHeap)
                heapq.heappush(self.downHeap, -temp)
            else:
                temp = heapq.heappop(self.downHeap)
                heapq.heappush(self.upHeap, -temp)

    def findMedian(self) -> float:
        if len(self.upHeap) == len(self.downHeap):
            return (self.upHeap[0] + (-self.downHeap[0])) / 2
        return self.upHeap[0] if len(self.upHeap) > len(self.downHeap) else -self.downHeap[0]

# 3, 1

# upheap   3
# downheap 1

# edge case: one of upheap or downheap is zero-length. we can know which heap shoud be fill by compare with heap non null. if they match with them, we store to them and if it's not match, we store to null heap

# and then after normal store, we rebalanced it oke


# both of array is zero length


# 3   1   5   4, 
#     |

# 1, 3, 4, 5, 5, 7
# upheap      = 5 5 7
# downheap    = 4 3 1
# median      = 

