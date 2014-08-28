public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int row = 0, col = 0, cycle = 0;
        List<Integer> result = new ArrayList<Integer>();
        while (row < matrix.length - row && col < matrix[0].length - col){
            // move right
            while (col < matrix[0].length - cycle)
                result.add(matrix[row][col++]);
            col--;
            row++;
            
            // move down
            if (row >= matrix.length - cycle) // no down position available
                break;
            while (row < matrix.length - cycle)
                result.add(matrix[row++][col]);
            row--;
            col--;
            
            // move left
            if (col < cycle) // no left position available
                break;
            
            while (col >= cycle)
                result.add(matrix[row][col--]);
            col++;
            row--;
            
            // move up
            while (row > cycle)
                result.add(matrix[row--][col]);
            cycle++;
            row = cycle;
            col = cycle;
        }
        return result;
    }
}