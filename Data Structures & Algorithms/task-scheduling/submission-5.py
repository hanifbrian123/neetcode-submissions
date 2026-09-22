class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = {}
        for ch in tasks:
            cnt[ch] = 1 + cnt.get(ch, 0)
        
        heap = [(-c, ch) for ch, c in cnt.items()]
        heapq.heapify(heap)
        q = collections.deque([])
        tasksLeft = len(tasks)
        i = 0

        def getFromQ():
            ch = q.popleft()[0]
            cnt[ch] -= 1
            if cnt[ch]:
                q.append([ch, i+n+1])
            
            
        def getFromHeap():
            c, ch = heapq.heappop(heap)
            cnt[ch] -= 1
            if cnt[ch]:
                q.append([ch, i+n+1])

        while tasksLeft > 0:
            if q and i >= q[0][1] and heap:
                if cnt[q[0][0]] >= -heap[0][0]:
                    getFromQ()
                else:
                    getFromHeap()
                tasksLeft -= 1
            elif q and i >= q[0][1]:
                getFromQ()
                tasksLeft -= 1
            elif heap:
                getFromHeap()
                tasksLeft -= 1
            else:
                i = q[0][1] - 1
            
            i+=1
        return i