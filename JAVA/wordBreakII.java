public class Solution {
    public ArrayList<String> wordBreak(String s, Set<String> dict) {
        List<List<Integer>> positions = new ArrayList<List<Integer>>();
        for(int i=0; i<s.length(); i++)
            positions.add(new ArrayList<Integer>());
            
        Boolean[] dp = new Boolean[s.length()];
        
        for(int j = 0; j< s.length(); j++)
            dp[j] = false;
            
        for(int end = 1; end <= s.length(); end++)
            for(int start = 0; start < end; start++)
                if ((start == 0 || dp[start-1]) && dict.contains(s.substring(start, end))){
                    dp[end-1] = true;
                    positions.get(end-1).add(start);
                }
                
        if (!dp[s.length()-1])
            return new ArrayList<String>();
            
        // rebuild strings
        List<List<String>> result = new ArrayList<List<String>>(s.length());
        for(int i=0; i<s.length(); i++)
            result.add(new ArrayList<String>());
            
        List<String> cur, target;
        String tail;
        for(int end = 1; end <= s.length(); end++){
            target = result.get(end-1);
            for(int start:positions.get(end-1)){
                if (end == s.length())
                    tail = "";
                else
                    tail = " ";
                
                if (start == 0)
                    target.add(s.substring(start,end)+tail);
                else
                    for(String head:result.get(start-1))
                        target.add(head+s.substring(start,end)+tail);
            }
        }
        return (ArrayList<String>) result.get(s.length()-1);
    }
}

// USE DP, DFS WONT WORK

// public class Solution {
//     public ArrayList<String> wordBreak(String s, Set<String> dict) {
//         ArrayList<String> result = new ArrayList<String>();
//         if (s.isEmpty())
//             return result;
//         return dfs(0, s, dict);
//     }
//     public ArrayList<String> dfs(int start, String s, Set<String> dict){
//         ArrayList<String> result = new ArrayList<String>(), rest;
//         if (start == s.length()){
//             result.add("");
//             return result;
//         }
//         for (int i=start+1;i<s.length();i++){
//             if (dict.contains(s.substring(start, i))){
//                 rest = dfs(i, s, dict);
//                 for (String temp:rest)
//                     if (temp.isEmpty())
//                         result.add(s.substring(start,i));
//                     else
//                         result.add(s.substring(start,i)+" "+temp);
                
//             }
//         }
//         return result;
//     }
// }