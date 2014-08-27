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
    public ListNode partition(ListNode head, int x) {
        ListNode p = head, greaterHead = null, greaterTail = null, lessHead = null, lessTail = null;
        while (p!=null){
            if (p.val >= x){
                if (greaterHead == null){
                    greaterHead = p;
                    greaterTail = p;
                }
                else{
                    greaterTail.next = p;
                    greaterTail = greaterTail.next;
                }
                p = p.next;
                greaterTail.next = null;
            }
            else{
                if (lessHead == null){
                    lessHead = p;
                    lessTail = p;
                }
                else{
                    lessTail.next = p;
                    lessTail = lessTail.next;
                }
                p = p.next;
                lessTail.next = null;
            }
        }
        if (lessHead != null){
            lessTail.next = greaterHead;
            return lessHead;
        }
        return greaterHead;
    }
}