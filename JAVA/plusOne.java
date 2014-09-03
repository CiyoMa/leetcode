public class Solution {
    public int[] plusOne(int[] digits) {
        int end = digits.length - 1, carry = 1 , temp;
        while (end >= 0 && carry == 1){
            temp = (digits[end] + carry) / 10;
            digits[end] = (digits[end] + carry) % 10;
            carry = temp;
            end--;
        }
        if (end < 0 && carry == 1){
            int[] result = new int[digits.length + 1];
            result[0] = 1;
            for (int i= 1; i < digits.length+1; i++)
                result[i] = digits[i-1];
            return result;
        }
        return digits;
    }
}