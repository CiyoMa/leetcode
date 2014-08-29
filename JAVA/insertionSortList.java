// Solution 1

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
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode last = head, cur=head.next, next, temp, p, q;
        while(cur != null){
            next = cur.next;
            if (head.val > cur.val){
                cur.next = head;
                last.next = next;
                head = cur;
                cur = next;
                continue;
            }
            
            q = null;
            temp = head;
            while(temp != last && temp.val <= cur.val){
                q = temp;
                temp = temp.next;
            }
            if (temp.val <= cur.val){ // important, cannot change to temp != last, since they can be both unsatisfied, 4213 -> 1243
                last = cur;
                cur = next;
                continue;
            }
            else{
                p = q.next;
                q.next = cur;
                cur.next = p;
                last.next = next;
                cur = next;
            }
        }
        return head;
    }
}

// Solution 2

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
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode last = head, cur=head.next, next, temp, p, q;
        while(cur != null){
            next = cur.next;
            if (head.val > cur.val){
                cur.next = head;
                last.next = next;
                head = cur;
                cur = next;
                continue;
            }
            if (last.val <= cur.val){
                last = cur;
                cur = next;
                continue;
            }
            q = null;
            temp = head;
            while(temp != last && temp.val <= cur.val){
                q = temp;
                temp = temp.next;
            }
            p = q.next;
            q.next = cur;
            cur.next = p;
            last.next = next;
            cur = next;
        }
        return head;
    }
}