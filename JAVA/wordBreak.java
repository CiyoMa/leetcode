public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        Boolean[] seg = new Boolean[s.length()];
        for (int i=0; i< s.length(); i++)
            seg[i] = false;
        for (int end = 1; end <= s.length(); end++)
            for (int start = 0; start < end; start++)
                if ((start == 0 || seg[start-1]) && dict.contains(s.substring(start, end))){
                    seg[end-1] = true;
                    break;
                }
        return seg[s.length()-1];
    }
}