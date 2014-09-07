public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<Character>();
        char last;
        for(char c : s.toCharArray()){
            if (c == '(' || c == '[' || c == '{')
                stk.push(c);
            else{
                if(stk.isEmpty())
                    return false;
                last = stk.pop();
                if(last == '(' && c == ')' || last == '[' && c == ']' || last == '{' && c == '}')
                    continue;
                return false;
            }
        }
        return stk.isEmpty();
    }
}