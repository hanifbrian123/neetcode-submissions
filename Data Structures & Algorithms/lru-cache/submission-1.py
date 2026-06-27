class Node:
    def __init__(self, val = None, key = None, next: Node = None, prev: Node = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.least = Node()
        self.most = Node()

        self.least.prev = None
        self.least.next = self.most
        self.most.prev = self.least
        self.most.next = None

        self.capacity = capacity
        self.keyToNode = {}
    def get(self, key: int) -> int:
        # return -1 if there is no
        if self.keyToNode.get(key, None) is None:
            return -1

        # if there, return the value and move to most
        ## get node address and its value
        ret = self.keyToNode[key].val

        ## move to the most
        ### evict the node first
        nodeAdd = self.keyToNode[key]
        prevTemp = nodeAdd.prev
        nextTemp = nodeAdd.next

        prevTemp.next = nextTemp
        nextTemp.prev = prevTemp

        ### move to the most
        prevTemp = self.most.prev
        nextTemp = self.most

        prevTemp.next = nodeAdd
        nodeAdd.prev = prevTemp
        nodeAdd.next = nextTemp
        nextTemp.prev = nodeAdd

        # Return 
        return ret


    def put(self, key: int, value: int) -> None:
        # Jika sudah ada di cache
        if self.keyToNode.get(key, None) is not None:
            # putus dan sambung di tengah
            nodeAdd = self.keyToNode[key]
            prevTemp = nodeAdd.prev
            nextTemp = nodeAdd.next
            prevTemp.next = nextTemp
            nextTemp.prev = prevTemp

            # putus most dan top, then insert nodeAdd
            prevTemp = self.most.prev
            nextTemp = self.most

            prevTemp.next = nodeAdd
            nodeAdd.prev = prevTemp
            nodeAdd.next = nextTemp
            nextTemp.prev = nodeAdd

            # set value nya jangan lupa
            nodeAdd.val = value
        # jika kapasitas masih ada => langsung tambahkan, dan kurangi cap
        elif self.capacity:
            # tambahkan ke previous most
            nextTemp = self.most
            prevTemp = self.most.prev

            newNode = Node(value, key)
            prevTemp.next = newNode
            newNode.prev = prevTemp
            newNode.next = nextTemp
            nextTemp.prev = newNode

            # kurangi cap
            self.capacity -= 1

            # jangan lupa tambahkan ke key to node
            self.keyToNode[key] = newNode
        # jika kapasitas sudah tidak ada => tambahkan ke most dan hapus el yang ada di least
        else:
            # taruh di most
            prevTemp = self.most.prev
            nextTemp = self.most

            newNode = Node(value, key)
            prevTemp.next = newNode
            newNode.prev = prevTemp
            newNode.next = nextTemp
            nextTemp.prev = newNode

            # tambahkan ke key to node
            self.keyToNode[key] = newNode

            # evict node least
            prevTemp = self.least
            midTempToEvict = prevTemp.next
            nextTemp = prevTemp.next.next

            prevTemp.next = nextTemp
            nextTemp.prev = prevTemp

            # evict node berarti hapus key to node nya juga
            del self.keyToNode[midTempToEvict.key]





#     def __init__(self, capacity: int):
#         self.head = None
#         self.tail = None
#         self.capacity = capacity
#         self.keyToNode = {}
#     def get(self, key: int) -> int:

#     def put(self, key: int, value: int) -> None:
#         if self.keyToNode.get(key, None) is not None:
#             keyNode = self.keyToNode[key]

#             if self.tail == keyNode:
#                 self.tail

#             tempPrev = keyNode.prev
#             tempNext = keyNode.next
            
#             tempPrev.next = tempNext
#             tempNext.prev = tempPrev
            
#             keyNode.next = self.head
#             keyNode.prev = None
            
#             self.head = keyNode

#             keyNode.val = value
#         elif capacity:






#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.head = Node()
#         self.current = self.head
#         self.keyToNodeAdd = {}
        

#         print(self.capacity)
#         print(self.head, self.current)
#         print(self.keyToNodeAdd)
#         print("================")
#         print()
#     def get(self, key: int) -> int:
#         print()
#         print()
#         print("GET: ", self.keyToNodeAdd[key].val if self.keyToNodeAdd.get(key, None) is not None else -1)
#         return self.keyToNodeAdd[key].val if self.keyToNodeAdd.get(key, None) is not None else -1

#     def put(self, key: int, value: int) -> None:
#         print()
#         print()
#         print("PUT: ", key, value)
#         if self.keyToNodeAdd.get(key, None) is not None:
#             nodeAdd = self.keyToNodeAdd[key]
#             nodeAdd.val = value
#             nodeAdd.key = key
#             return
        
#         if self.capacity:
#             self.current.val = value
#             self.current.key = key
#             self.keyToNodeAdd[key] = self.current

#             self.current.next = Node(-1)
#             self.current = self.current.next
#             self.capacity -= 1
            
#         else:
#             print("TESTT: ", self.current, self.current.val, self.head)
#             print(self.keyToNodeAdd)
#             if self.current.val == -1:
#                 self.current = self.head
#             del self.keyToNodeAdd[self.current.key]
#             self.current.val = value
#             self.current.key = key
#             self.keyToNodeAdd[key] = self.current

#             self.current = self.current.next
#         print("PRINT LL", "head: ", self.head.val)
#         self.printLinkedList()

#         print(self.keyToNodeAdd)

#     def printLinkedList(self):
#         curr = self.head
#         while curr:
#             print(curr.val, end=' ')
#             curr = curr.next
#         print()
        



# Kondisi:
# - put:
#     - sudah ada => pop dia lalu taruh most. if most itu dia maka biarkan ,ganti valuenya saja
#     - biasa (masih kosong)
# - biasa (masih kosong)
# - ketika penuh, put di most, tapi ganti least dengan next nya
# - sudah ada:
#     - if element ini adalah least dan most, maka tetap harusnya (biarkan spt itu)
#     - pindah ke most.
#     - ganti val nya
#     - sambungkan prev dan next nya