class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.mp = {}
        self.head = Node()
        
        cur = self.head
        
        # Build linkedlist
        for i in range(1, capacity):
            newNode = Node()
            cur.nxt = newNode
            cur = cur.nxt

        self.cur = self.head


    def get(self, key: int) -> int:
        node = self.mp.get(key, None)
        return node.value if node is not None else -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.value = value
        else:
            self.mp[key] = self.cur

            if self.cur.key is not None:
                del self.mp[self.cur.key]
            
            self.cur.key = key
            self.cur.value = value
            self.cur = self.cur.nxt
            if self.cur is None:
                self.cur = self.head





# (1, 10), (2, 20)

# get:
# - get value base on key

# put:
# case i (key exist): change the value by the address from the key
# case ii (key not exist):
#     map[key] = curr add
#     case i (if cur doesnt have any value):
#         - cur -> (value)
#     case ii (if cur have any value):
#         - evict value from cur
#         - evict key from map
#         - cur -> (value)
#     - cur = cur.next
#     - if curr is none:
#         cur = dummy.next

# cap = 3
# cur: add = 
# map = {key: add}

