/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode tail = dummyHead, cur = head, temp;
        while (cur!= null && cur.next != null){
            tail.next = cur.next;
            temp = cur.next.next;
            cur.next.next = cur;
            cur.next = temp;
            tail = cur;
            cur = tail.next;
        }
        return dummyHead.next;
    }
}