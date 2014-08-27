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
    public void reorderList(ListNode head) {
        if (head == null || head.next == null)
            return;
        ListNode half = head, backHalf, p, temp, end = head.next;
        while (end != null){
            end = end.next;
            if (end != null){
                half = half.next;
                end = end.next;
            }
        }
        backHalf = half.next;
        half.next = null;
        
        // reverse backHalf
        p = backHalf.next;
        backHalf.next = null;
        while (p != null){
            temp = p.next;
            p.next = backHalf;
            backHalf = p;
            p = temp;
        }
        
        //interleaf
        ListNode nextQ, nextP, q;
        q = head;
        p = backHalf;
        while (p != null){
            nextQ = q.next;
            nextP = p.next;
            q.next = p;
            p.next = nextQ;
            q = nextQ;
            p = nextP;
        }
        return;
    }
}