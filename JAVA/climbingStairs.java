public class Solution {
    public int climbStairs(int n) {
        if (n==1)
            return 1;
        int last = 1, cur =2, count=0, temp;
        while (count++<n-2){
            temp = cur;
            cur = cur+last;
            last = temp;
        }
        return cur;
    }
}