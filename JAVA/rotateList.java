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
    public ListNode rotateRight(ListNode head, int n) {
        int length = 0;
        ListNode p = head, tail = head, rotated;
        while (p != null){
            length++;
            tail = p;
            p = p.next;
        }
        if (length <= 1 || n % length == 0)
            return head;
        length = length - 1 - n % length;
        p = head;
        while (length > 0){
            p = p.next;
            length--;
        }
        rotated = p.next;
        tail.next = head;
        p.next = null;
        return rotated;
    }
}