public class Solution {
    private static char[] p;
    
    public ArrayList<ArrayList<String>> partition(String s) {
        p = s.toCharArray();
        return dfs(0);
    }
    
    public ArrayList<ArrayList<String>> dfs(int start){
        ArrayList<ArrayList<String>> rest, result = new ArrayList<ArrayList<String>>();
        if (start == p.length){
            result.add(new ArrayList<String>());
            return result;
        }
        for (int end = start; end < p.length; end++){
            if (isPalindrome(start, end)){
                rest = dfs(end + 1);
                for (ArrayList<String> als: rest){
                    als.add(0, new String(p, start, end-start+1));
                }
                result.addAll(rest);
            }
        }
        return result;
    }
    
    public Boolean isPalindrome(int start, int end){
        while (start < end)
            if (p[start++]!=p[end--])
                return false;
        return true;
    }
}