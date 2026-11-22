class ListNode {
    private int key, value;
    private ListNode next, prev;
    public ListNode(int key, int value) {
        this.key = key; this.value = value;
    }
}
class LRUCache {
    private int cap;
    private Map<Integer, ListNode> map = new HashMap<>();
    private ListNode least = new ListNode(-1, -1);
    private ListNode most = new ListNode(-1, -1);
    
    public LRUCache(int capacity) {
        least.next = most;
        most.prev = least;

        cap = capacity;
    }
    
    public int get(int key) {
        ListNode node;
        if (map.containsKey(key)) {
            node = map.get(key);
            node.prev.next = node.next;
            node.next.prev = node.prev;
            moveUp(node);
            return node.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        ListNode node;
        if (map.containsKey(key)) {
            node = map.get(key);
            node.prev.next = node.next;
            node.next.prev = node.prev;
        } else {
            node = new ListNode(key, value);
            map.put(key, node);
        }
        
        moveUp(node);
        
        node.value = value;

        if (map.size() > cap) {
            // evict lru
            ListNode lru = least.next;
            least.next = lru.next;
            lru.next.prev = least;
            map.remove(lru.key);
        }
    }
    

    public void moveUp(ListNode node) {
        node.next = most;
        node.prev = most.prev;
        
        ListNode temp = most.prev;
        most.prev = node;
        temp.next = node;
    }
}



// cap = 2
// mostrecent = #aaa
// lru = (1, 10) | (3, 20), (2, 90)
// map = {
//     3: #c
//     2: #b
// }