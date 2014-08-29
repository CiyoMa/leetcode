public class Solution {
    public String addBinary(String a, String b) {
        int i=a.length()-1, j=b.length()-1, carry=0, temp;
        String result = "";
        while (i>=0 && j>=0){
            temp = Character.getNumericValue(a.charAt(i)) + Character.getNumericValue(b.charAt(j)) + carry;
            carry = temp/2;
            result = Integer.toString(temp%2) + result;
            i--;
            j--;
        }
        while (i>=0){
            temp = Character.getNumericValue(a.charAt(i)) + carry;
            carry = temp/2;
            result = Integer.toString(temp%2) + result;
            i--;
        }
        while (j>=0){
            temp = Character.getNumericValue(b.charAt(j)) + carry;
            carry = temp/2;
            result = Integer.toString(temp%2) + result;
            j--;
        }
        if (carry == 1)
            result = "1"+result;
        return result;
    }
}