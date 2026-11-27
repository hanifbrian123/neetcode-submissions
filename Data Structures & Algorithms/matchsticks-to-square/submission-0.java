class ListNode {
    private int value;
    private ListNode prev;
    private ListNode next;

    ListNode(int value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}
class Solution {
    private ListNode head = new ListNode(0);
    private ListNode tail = new ListNode(0);
    public boolean makesquare(int[] matchsticks) {
        head.next = tail; tail.prev = head;
        int sumMs = Arrays.stream(matchsticks).sum();
        if (sumMs % 4 != 0) return false;

        for (int i = 0; i < matchsticks.length; i++) matchsticks[i] = -matchsticks[i];
        Arrays.sort(matchsticks);
        for (int i = 0; i < matchsticks.length; i++) matchsticks[i] = -matchsticks[i];

        ListNode prev = head;
        ListNode next = tail;
        for (int i = 0; i < matchsticks.length; i++) {
            ListNode node = new ListNode(matchsticks[i]);
            putBetween(prev, next, node);
            prev = node;
        }

        for (int i = 0; i < 4; i++) {
            ListNode cur = head.next;
            int sum = 0;
            while (cur.value != 0 && sum < sumMs / 4) {
                if (sum + cur.value <= sumMs / 4) {
                    sum += cur.value;
                    evict(cur);
                };
                cur = cur.next;
            }
            if (sum != sumMs / 4) return false;
        }
        return true;

        
    }

    private void putBetween(ListNode prev, ListNode next, ListNode node) {
        prev.next = node;
        node.prev = prev;
        node.next = next;
        next.prev = node;
    }
    private void evict(ListNode node) {
        node.prev.next = node.next;
        node.next = node.prev;
    }
}

// 1,3,4,2,2,4 => 16
// 4 4 3 2 2 1
// 4 -> 4 -> 3 + 1 -> 2 + 2

// 6 -> 6 -> 4 -> 1 -> 1 -> 2


// 6 6 3 1 1 1 2 2 2


// 7 7 3 2 