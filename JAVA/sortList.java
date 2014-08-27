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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) 
            return head;
        ListNode temp, half = head, end = head.next;
        while(end != null){
            end = end.next;
            if (end != null){
                half = half.next;
                end = end.next;
            }
        }
        temp = half.next;
        half.next = null;
        return merge(sortList(head), sortList(temp));
    }
    public ListNode merge(ListNode p, ListNode q){
        ListNode temp, head = null, tail = null;
        if (p == null || q == null) return p == null? q:p;
        while (p!=null && q!=null){
            temp = p.val > q.val? q:p;
            if (head == null){
                head = temp;
                tail = temp;
            }
            else{
                tail.next = temp;
                tail = tail.next;
            }
            p = temp == p? p.next:p;
            q = temp == q? q.next:q;
            tail.next = null;
        }
        if (p!=null || q!=null)
            tail.next = p==null? q:p;
        return head;
    }
}