public class Solution {
    public String countAndSay(int n) {
        int count = 1, temp;
        String val = "1", next;
        char lastChar = ' ';
        while (count < n){
            next = "";
            temp = 1;
            lastChar = ' ';
            for (char ch:val.toCharArray()){
                if (lastChar == ' ')
                    lastChar = ch;
                else if (lastChar == ch)
                    temp += 1;
                else{
                    next += Integer.toString(temp) + lastChar;
                    temp = 1;
                    lastChar = ch;
                }
            }
            next += Integer.toString(temp) + lastChar;
            count++;
            val = next;
        }
        return val;
    }
}