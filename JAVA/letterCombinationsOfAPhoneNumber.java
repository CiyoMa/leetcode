public class Solution {
    public ArrayList<String> letterCombinations(String digits) {
        ArrayList<String> result = new ArrayList<String>();
        ArrayList<String> restResult; //= new ArrayList<String>();
        if (digits.length() == 0){
            result.add("");
            return result;
        }
        char digit = digits.charAt(0);
        digits = digits.substring(1);
        String[] dic = new String[]{"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

        restResult = letterCombinations(digits);
        for (int i=0; i<restResult.size(); i++)
            for (int j = 0; j < dic[digit-'2'].length(); j++)
                result.add(dic[digit-'2'].charAt(j) + restResult.get(i));
        return result;
    }
}