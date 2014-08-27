public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int i = matrix.length;
        if (i < 1) 
            return false;
        int j = matrix[0].length;
        if (j < 1)
            return false;
        if (matrix[0][0] > target || matrix[i-1][j-1] < target)
            return false;
        int mid, low = 0, high = i - 1, row;
        while(low <= high){
            mid = (low + high)/2;
            if (matrix[mid][0] > target)
                high = mid - 1;
            else if (matrix[mid][0] == target)
                return true;
            else if (mid < high && matrix[mid][0] < target && matrix[mid+1][0] > target || mid == high && matrix[mid][0] < target){
                low = mid;
                high = mid;
                break;
            }
            else
                low = mid + 1;
        }
        row = low;
        low = 0;
        high = j - 1;
        while(low <= high){
            mid = (low + high) / 2;
            if (matrix[row][mid] == target)
                return true;
            else if(matrix[row][mid] > target)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return false;
    }
}