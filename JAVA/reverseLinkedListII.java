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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (n - m == 0) 
            return head;
            
        ListNode reverseHead, cur, next, tail, before=head;
        int count = 1;
        
        cur = head;
        while (count < m-1 && cur != null){
            cur = cur.next;
            count++;
        }
        
        if (m == 1){
            reverseHead = head;
            tail = head;
            cur = head.next;
            count++;
        }
        else{
            before = cur;
            reverseHead = cur.next;
            tail = cur.next;
            cur = tail.next;
            count+=2;
        }
        while (count <= n && cur != null){
            next = cur.next;
            cur.next = reverseHead;
            reverseHead = cur;
            cur = next;
            tail.next = next;
            count++;
        }
        if (m != 1) 
            before.next = reverseHead;
        return (m == 1)? reverseHead : head;
    }
}