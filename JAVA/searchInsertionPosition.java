public class Solution {
    public int searchInsert(int[] A, int target) {
        int begin = 0, end = A.length-1, mid;
        while (begin <= end){
            mid = begin + end;
            mid /= 2;
            if (A[mid] == target || (mid > begin && A[mid-1] < target && A[mid] > target))
                return mid;
            else if (A[mid] > target)
                end = mid - 1;
            else
                begin = mid + 1;
        }
        return begin;
    }
}