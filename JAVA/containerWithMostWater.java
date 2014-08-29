public class Solution {
    public int maxArea(int[] height) {
        int max = 0, begin = 0, end = height.length-1, cur, temp;
        while (begin < end){
            cur = (end - begin) * (height[begin] > height[end]? height[end]:height[begin]);
            max = max > cur? max:cur;
            if (height[begin] <= height[end]){
                temp = height[begin];
                while (begin < end && height[begin] <= temp)
                    begin++;
            }
            else{
                temp = height[end];
                while (begin < end && temp >= height[end])
                    end--;
            }
        }
        return max;
    }
}