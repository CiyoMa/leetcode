public class Solution {
    public boolean isPalindrome(String s) {
        if (s.isEmpty()) 
            return true;
        char[] p = s.toCharArray();
        int low = 0, high = p.length - 1;
        while (low < high){
            if (p[low] >= 'A' && p[low] <= 'Z')
                p[low] += 'a' - 'A';
            if (p[high] >= 'A' && p[high] <= 'Z')
                p[high] += 'a' - 'A';
            if (p[low] < '0' || p[low] > '9' && p[low] < 'a' || p[low] > 'z')
                low++;
            else if (p[high] < '0' || p[high] > '9' && p[high] < 'a' || p[high] > 'z')
                high--;
            else if (p[low] != p[high])
                return false;
            else{
                low++;
                high--;
            }
        }
        return true;
    }
}