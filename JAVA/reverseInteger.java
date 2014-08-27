public class Solution {
    public int reverse(int x) {
        int sign = 1, reverse = 0;
        if (x < 0) {
            sign = -1; 
            x *= -1;
        }
        while (x > 0){
            reverse *= 10;
            reverse += x % 10;
            x /= 10;
        }
        return reverse*sign;
    }
}