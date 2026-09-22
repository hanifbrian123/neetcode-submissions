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
        while tasksLeft > 0:
            if q and q[0][1] == i:
                ch = q.popleft()[0]
                cnt[ch] -= 1
                tasksLeft -= 1
                if cnt[ch]:
                    q.append([ch, i+n+1])
            elif heap:
                c, ch = heapq.heappop(heap)
                cnt[ch] -= 1
                tasksLeft -= 1
                if cnt[ch]:
                    q.append([ch, i+n+1])
            
            i+=1
        return i



# a: 1
# b: 1
# c: 1

# a -> b -> c ->idl-> a -> b -> c ->idl-> a
# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# q = [a, 4] | q = [b, 5], [c, 6]


# if i == q.peek[1]: taruh q.peek[0]
# else if maxheap.length: taruh max_heap.pop
# else: taruh idle
