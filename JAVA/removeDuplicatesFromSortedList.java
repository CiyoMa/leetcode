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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode currentEnd = head, probe;
        if (head == null) return head;
        probe = head.next;
        while (probe != null){
            while (probe != null && probe.val == currentEnd.val)
                probe = probe.next;
            currentEnd.next = probe;
            currentEnd = probe;
        }
        return head;
    }
}