public class Solution {
    public int sqrt(int x) {
        if (x < 1)
            return 0;
        if (x < 4)
            return 1;
            
        float quotient;
        int low = 0, high = x, mid;
        while (low < high){
            mid = (low + high) / 2;
            if (x / mid >= mid && x / (mid + 1) < (mid + 1))
                return mid;
            else if (x / mid >= mid)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return low;
    }
}