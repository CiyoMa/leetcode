public class Solution {
    public String minWindow(String S, String T) {
        if (S.equals("") || T.equals(""))
            return "";
        int[] target = new int[255];
        int[] current = new int[255];
        for (int j=0; j<255; j++){
            target[j] = 0;
            current[j] = 0;
        }
        for (int i = 0; i < T.length(); i++)
            target[(int) T.charAt(i)] += 1;
            
        Boolean hasT = false;
        int start = -1, i = 0;
        while (i < S.length() && !isMatched(current, target)){
            if (start == -1 && target[(int) S.charAt(i)] > 0)
                start = i;
            current[(int) S.charAt(i++)] += 1;
        }
        if (start == -1 || !isMatched(current, target))
            return "";
        int cur = (int) S.charAt(start);
        while (target[cur] == 0 || current[cur] > target[cur]){
            if (current[cur] > target[cur])
                current[cur] -= 1;
            cur = (int) S.charAt(++start);
        }
        
        int bestStart = start;
        int end = i, len = end - start;
        while (end < S.length()){
            cur = (int) S.charAt(end);
            if (target[cur] > 0)
                current[cur] += 1;
            if (S.charAt(end) == S.charAt(start)){
                cur = (int) S.charAt(start);
                while (target[cur] == 0 || current[cur] > target[cur]){
                    if (current[cur] > target[cur])
                        current[cur] -= 1;
                    cur = (int) S.charAt(++start);
                }
                if (len > end - start + 1){
                    bestStart = start;
                    len = end - start + 1;
                }
            }
            end++;
        }
        return S.substring(bestStart, bestStart + len);
    }
    
    public Boolean isMatched(int[] current, int[] target){
        for (int i = 0; i < 255; i++)
            if (current[i] < target[i])
                return false;
        return true;
    }
}