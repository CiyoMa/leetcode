public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        Boolean[] visited = new Boolean[n];
        for (int i = 0; i < visited.length; i++)
            visited[i] = false;
        return dfs(0, visited, k, n);
    }
    
    public List<List<Integer>> dfs(int start, Boolean[] visited, int remainK, int n){
        ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        List<List<Integer>> rest;
        if (remainK == 0){
            result.add(new ArrayList<Integer>());
            return result; 
        }
        for (int j=start; j<n; j++){
            if (visited[j]) 
                continue;
            visited[j] = true;
            rest = dfs(j+1, visited, remainK-1, n);
            for(List<Integer> lst: rest){
                lst.add(0, j+1);
                result.add(lst);
            }
            visited[j] = false;
        }
        return result;
    }
}