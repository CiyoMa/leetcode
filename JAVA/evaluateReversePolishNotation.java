public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<Integer>();
        int op1, op2;
        for (String t:tokens ){
            if (t.equals("+")){
                op1 = st.pop();
                op2 = st.pop();
                st.push(op1+op2);
            }
            else if (t.equals("-")){
                op1 = st.pop();
                op2 = st.pop();
                st.push(op2 - op1);
            }
            else if (t.equals("*")){
                op1 = st.pop();
                op2 = st.pop();
                st.push(op1 * op2);
            }
            else if (t.equals("/")){
                op1 = st.pop();
                op2 = st.pop();
                st.push(op2 / op1);
            }
            else
                st.push(Integer.parseInt(t));
        }
        return st.pop();
    }
}