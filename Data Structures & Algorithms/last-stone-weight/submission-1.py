class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            firstLarge = heapq.heappop(heap)
            secondLarge = heapq.heappop(heap)
            heapq.heappush(heap, firstLarge - secondLarge)
        return -heap[0] if heap else 0
        