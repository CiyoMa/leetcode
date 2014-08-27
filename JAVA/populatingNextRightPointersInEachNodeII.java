/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        TreeLinkNode currentLevel, nextLevel, nextBegin;
        currentLevel = root;
        nextLevel = null;
        nextBegin = null;
        while (currentLevel != null){
            if (currentLevel.left != null) {
                if (nextBegin == null){
                    nextBegin = currentLevel.left;
                    nextLevel = nextBegin;
                }
                else{
                    nextLevel.next = currentLevel.left;
                    nextLevel = nextLevel.next;
                }
            }
            if (currentLevel.right != null) {
                if (nextBegin == null){
                    nextBegin = currentLevel.right;
                    nextLevel = nextBegin;
                }
                else{
                    nextLevel.next = currentLevel.right;
                    nextLevel = nextLevel.next;
                }
            }
            if (currentLevel.next != null)
                currentLevel = currentLevel.next;
            else{
                currentLevel = nextBegin;
                nextBegin = null;
            }
        }
    }
}