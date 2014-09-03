public class Solution {
    public int lengthOfLastWord(String s) {
        int len = 0, i = 0, lastLen = 0;
        while (i < s.length()){
            if (s.charAt(i++) == ' '){
                lastLen = len > 0? len:lastLen;
                len = 0;
            }
            else
                len += 1;
        }
        return len > 0? len:lastLen;
    }
}