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
        if (head == null || head.next == null)
            return head;
        ListNode dummyHead = new ListNode(0);
        ListNode p = head, q = head.next, tail=dummyHead;
        while (p!=null){
            if (q == null || p.val != q.val){
                tail.next = p;
                p.next = null;
                tail = tail.next;
                p = q;
                q = (q == null)? null:q.next;
                continue;
            }
            while (q!=null && p.val==q.val)
                q = q.next;
            p = q;
            q = (p == null)? null:p.next;
        }
        return dummyHead.next;
    }
}