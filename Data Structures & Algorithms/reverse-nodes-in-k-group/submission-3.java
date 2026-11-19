/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k == 1) return head;
        if (head.next == null) return head;
        
        ListNode dummyL = new ListNode(-1, head);
        ListNode dummyR = new ListNode(-1);
        int cnt = 1;
        ListNode cur = head;
        while (cur.next != null) {
            cnt++;
            cur = cur.next;
        }
        cur.next = dummyR;
        int numberOfGroup = cnt / k;

        ListNode prev = dummyL;
        ListNode mid = head;
        ListNode nxt = head.next;
        for (int i = 0; i < numberOfGroup; i++) {
            ListNode first = mid;

            for (int j = 0; j < k; j++) {
                mid.next = prev;
                ListNode temp = mid;
                mid = nxt;
                prev = temp;
                nxt = nxt.next;
            }
            first.next.next = prev;
            first.next = mid;
            prev = first;
        }

        cur = dummyL.next;
        while (cur.next.val != -1) {
            cur = cur.next;
        }
        cur.next = null;

        return dummyL.next;
    }
}

// -1 -> 3 -> 2 -> 1 -> 4 -> 5 -> 6 -> -1 -> null
// -1 <- 1 <- 2 <- 3  4 -> 5 -> 6 -> -1 -> null
