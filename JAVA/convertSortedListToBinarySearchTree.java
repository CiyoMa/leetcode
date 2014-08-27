/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) 
            return null;
        if (head.next == null)
            return new TreeNode(head.val);
            
        ListNode half = head, end = head.next, temp = null;
        while (end != null){
            end = end.next;
            if (end != null){
                temp = half;
                half = half.next;
                end = end.next;
            }
        }
        
        TreeNode root = new TreeNode(half.val), left, right;
        
        if (temp != null){
            temp.next = null;
            left = sortedListToBST(head);
        }
        else
            left = null;
        
        temp = half.next;
        half.next = null;
        
        right = sortedListToBST(temp);
        root.left = left;
        root.right = right;
        return root;
    }
}