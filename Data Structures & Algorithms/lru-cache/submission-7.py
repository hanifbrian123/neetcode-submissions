class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val

        self.prev = None
        self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.mp = {}
        self.cap = capacity

        self.dummyL = Node(-1, -1)
        self.dummyR = Node(-1, -1)
        self.dummyL.nxt = self.dummyR
        self.dummyR.prev = self.dummyL

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev

            self.putToMost(node)

            return node.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        # print(key, value, self.mp)
        # print("++++++++++", self.dummyL.nxt.key, self.dummyL.nxt.val, "+++++")
        # self.showLL()
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev

            self.putToMost(node)
        else:
            node = Node(key, value)
            self.mp[key] = node

            self.putToMost(node)

        if len(self.mp) > self.cap:
            lru = self.dummyL.nxt
            l, r = lru.prev, lru.nxt
            l.nxt, r.prev = r, l
            del self.mp[lru.key]
        
        
    def putToMost(self, node):
        l = self.dummyR.prev
        r = self.dummyR
        
        l.nxt = node
        node.prev = l
        node.nxt = r
        r.prev = node

    def showLL(self):
        print("======== PRINT LL =========")
        cur = self.dummyL
        while cur is not None:
            print('( ', cur.key, cur.val, ' )', end=' ')
            cur = cur.nxt
        print()

        cur = self.dummyR
        while cur is not None:
            print('(', cur.key, cur.val, ')', end=' ')
            cur = cur.prev
        print()
        
        print()
        print()


"""
put (1, 10), get (1), put (2, 20), put(3, 30), get(2), get(1)

PUT
if key exist in mp
- move to most
- change value from the node
elif key not exist
- crate new node
- adding to the most

if cap <= 0
- eivct least
else
- cap--

GET
if exist
- move to most
- => node.val
eli key not exist
- => -1

Node:
- prev
- nxt
- key
- val

cap = 2
mp = {1}
dummy left
dummy right
ll = (-1, -1) -> (1, 10) -> (-1, -1) -> None
"""
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

