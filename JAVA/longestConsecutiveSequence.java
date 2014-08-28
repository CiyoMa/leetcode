public class Solution {
    public int longestConsecutive(int[] num) {
        Set<Integer> s = new HashSet<Integer>();
        int longest = 1, next, last, len;
        
        for (int n:num)
            s.add(n);
        
        Iterator<Integer> i = s.iterator();
        for(int cur:num){
            len = 1;
            next = cur + 1;
            last = cur - 1;
            s.remove(cur);
            while (s.contains(next)){
                len++;
                s.remove(next);
                next++;
            }
            while (s.contains(last)){
                len++;
                s.remove(last);
                last--;
            }
            longest = (len > longest)? len:longest;
        }
        return longest;
    }
}