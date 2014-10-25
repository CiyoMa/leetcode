public class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0 || s.charAt(0) == '0')
            return 0;
            
        int[] ways = new int[s.length()];
        ways[0] = 1;
        for (int i = 1; i < s.length(); i++)
            if (s.charAt(i) - '0' == 0)
                ways[i] = (s.charAt(i-1) - '1' < 2 && s.charAt(i-1) - '1' >= 0)? (i - 2 >= 0 ? ways[i-2] : 1) : 0;
            else if (s.charAt(i) - '1' < 6 && s.charAt(i-1) - '1' == 1 || s.charAt(i-1) - '1' == 0 )
                ways[i] = (i - 2 >= 0 ? ways[i-2] : 1) + ways[i-1];
            else
                ways[i] = ways[i-1];
        return ways[s.length()-1];
    }
}