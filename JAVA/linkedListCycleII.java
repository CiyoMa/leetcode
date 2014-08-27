/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null)
            return null;
        ListNode p = head, q = head.next, temp = head;
        while (p != q && q != null){
            q = q.next;
            if (q == null)
                return null;
            q = q.next;
            p = p.next;
        }
        if (q == null)
            return null;
        p = p.next;
        while (temp != p){
            temp = temp.next;
            p = p.next;
        }
        return p;
    }
}