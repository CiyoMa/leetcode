/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null)
            return null;
        RandomListNode p = head, q = head.next, copyHead;
        while (p != null){
            q = p.next;
            p.next = new RandomListNode(p.label);
            p.next.next = q;
            p = q;
        }
        p = head;
        q = head.next;
        while(p!=null){
            q = p.next;
            q.random = p.random == null ? null:p.random.next;
            p = q.next;
        }
        copyHead = head.next;
        p = head;
        q = head.next;
        while (p!=null){
            q = p.next;
            p.next = q.next;
            p = p.next;
            if (p == null) 
                break;
            q.next = p.next;
        }
        return copyHead;
    }
}