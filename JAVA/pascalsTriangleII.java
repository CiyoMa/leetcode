public class Solution {
    public List<Integer> getRow(int rowIndex) {
        rowIndex++;
        ArrayList<Integer> lastRow = new ArrayList<Integer>();
        ArrayList<Integer> currentRow = new ArrayList<Integer>(), temp;
        currentRow.add(1);
        int count = 1;
        while (count++ < rowIndex){
            temp = lastRow; 
            lastRow = currentRow;
            currentRow = temp;
            currentRow.add(0,1);
            currentRow.add(1);
            for (int j = 1; j < currentRow.size()-1; j++)
                currentRow.set(j, Integer.valueOf(lastRow.get(j-1)+lastRow.get(j)));
        }
        return currentRow;
    }
}