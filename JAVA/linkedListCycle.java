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
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode one = head;
        ListNode two = head.next;
        while (two != null && one != two){
            one = one.next;
            two = two.next;
            if (two != null)
                two = two.next;
        }
        return one == two;
    }
}