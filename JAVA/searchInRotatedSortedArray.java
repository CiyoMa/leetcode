public class Solution {
    public int search(int[] A, int target) {
        int pivot = -1, low = 0, high = A.length-1, mid;
        while(low <= high){
            mid = (low + high) / 2;
            if ((mid > 0 && A[mid] > A[mid - 1] || mid == 0 ) && (mid < A.length-1 && A[mid] > A[mid+1])){
                pivot = mid;
                break;
            }
            else if (A[mid] > A[0])
                low++;
            else 
                high--;
        }
        low = (pivot == -1)? 0 :(target <= A[A.length-1]?  pivot+1: 0);
        high = (pivot == -1)? A.length-1 :(target <= A[A.length-1]?  A.length-1:pivot+1);
        while(low <= high){
            mid = (low + high) / 2;
            if (A[mid] == target)
                return mid;
            else if (A[mid] < target)
                low++;
            else 
                high--;
        }
        return -1;
    }
}