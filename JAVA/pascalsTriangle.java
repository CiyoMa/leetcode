public class Solution {
    public List<List<Integer>> generate(int numRows) {
        ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> temp, last;
        if (numRows < 1)
            return result;
            
        temp = new ArrayList<Integer>();
        temp.add(1);
        result.add(temp);
        if (numRows == 1)
            return result;
        
        temp = new ArrayList<Integer>();
        temp.add(1);
        temp.add(1);
        result.add(temp);
        if (numRows == 2)
            return result;
        
        int row = 3;
        while (row <= numRows){
            temp = new ArrayList<Integer>();
            temp.add(1);
            
            last = result.get(result.size()-1);
            for (int j = 0; j < last.size()-1; j++)
                temp.add(last.get(j) + last.get(j+1));
            temp.add(1);
            row++;
            result.add(temp);
        }
        return result;
    }
}