public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        int c = x, reverse = 0;
        while (c > 0){
            reverse = reverse * 10 + c % 10;
            c /= 10;
        }
        return x == reverse;
    }
}