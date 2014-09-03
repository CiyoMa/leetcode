public class Solution {
    public int[] searchRange(int[] A, int target) {
        //Binary Search Part
        int low = 0, high = A.length - 1, pos = -1, mid;
        while (low <= high){
            mid = (low + high) / 2;
            if (A[mid] == target){
                pos = mid;
                break;
            }
            if (A[mid] > target)
                high--;
            else
                low++;
        }
        
        int[] range = new int[2];
        range[0] = pos;
        range[1] = pos;
        
        if (pos == -1)
            return range;
            
        //else extend & get range;
        while(range[0] > 0 && A[range[0]-1] == target)
            range[0] -= 1;
        while(range[1] < A.length-1 && A[range[1]+1] == target)
            range[1] += 1;
        return range;
    }
}

// worst case: O(n)

// Try use binary search find lowerbound and upperbound, with worst case O(n)