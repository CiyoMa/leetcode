public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        ArrayList<Integer> lastRow = (ArrayList<Integer>) triangle.get(triangle.size()-1);
        ArrayList<Integer> currentRow = new ArrayList<Integer>();
        int count = triangle.size()-2;
        while (count >= 0){
            for (int i = 1; i < lastRow.size(); i++)
                currentRow.add(triangle.get(count).get(i-1) + Math.min(lastRow.get(i-1),lastRow.get(i)));
            count--;
            lastRow = currentRow;
            currentRow = new ArrayList<Integer>();
        }
        return lastRow.get(0);
    }
}