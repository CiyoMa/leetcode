public class Solution {
    public void setZeroes(int[][] matrix) {
        boolean zeroFirstRow = false, zeroFirstCol = false;
        for (int i=0; i<matrix.length; i++ ){
            for (int j=0; j<matrix[0].length; j++){
                if (i == 0 && !zeroFirstRow && matrix[i][j] == 0)
                    zeroFirstRow = true;
                if (j == 0 && !zeroFirstCol && matrix[i][j] == 0)
                    zeroFirstCol = true;
                if (matrix[i][j] == 0){
                    if (i != 0)
                        matrix[i][0] = 0;
                    if (j != 0)
                        matrix[0][j] = 0;
                }
            }
        }
        for (int i=1; i<matrix.length; i++ ){
            for (int j=1; j<matrix[0].length; j++){
                if (matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            }
        }
        if (zeroFirstRow)
            for (int i=0; i<matrix[0].length; i++)
                matrix[0][i] = 0;
        if (zeroFirstCol)
            for (int i=0; i<matrix.length; i++)
                matrix[i][0] = 0;
    }
}