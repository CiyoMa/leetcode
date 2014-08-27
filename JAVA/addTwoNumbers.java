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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int comp = 0, temp, value;
        ListNode p1 = l1, p2 = l2, tail = null, head = null;
        if (p1 == null) return p2;
        else if (p2 == null) return p1;
        while (p1 != null && p2 != null){
            temp = (p1.val + p2.val + comp) / 10;
            value = (p1.val + p2.val + comp) % 10;
            comp = temp;
            if (head == null){
                head = new ListNode(value);
                tail = head;
            }
            else{
                tail.next = new ListNode(value);
                tail = tail.next;
            }
            p1 = p1.next;
            p2 = p2.next;
        }
        if (p1 == null && p2 == null && comp == 1){
            tail.next = new ListNode(1);
            tail = tail.next;
            return head;
        }
        p1 = p2 == null? p1:p2;
        if (p1 != null){
            if (comp == 0){
                tail.next = p1;
                return head;
            }
            else{
                while (p1!=null && comp != 0){
                    temp = (p1.val + comp) / 10;
                    value = (p1.val + comp) % 10;
                    comp = temp;
                    tail.next = new ListNode(value);
                    tail = tail.next;
                    p1 = p1.next;
                }
                if(p1==null && comp!= 0){
                    tail.next = new ListNode(1);
                    tail = tail.next;
                }
                else{
                    tail.next = p1;
                }
            }
        }
        
        return head;
        
    }
}