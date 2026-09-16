class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x in points:
            a, b = x[0], x[1]
            d = math.sqrt((a-0)**2 + (b-0)**2)
            heap.append(d)
        heapq.heapify(heap)
        minD = set()
        for i in range(k):
            minD.add(heapq.heappop(heap))
        res = []
        for x in points:
            a, b = x[0], x[1]
            d = math.sqrt((a-0)**2 + (b-0)**2)
            if d in minD:
                res.append(x)
            if len(res) == k:
                break
        return res
