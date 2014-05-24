class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        value = []
        for token in tokens:
        	if token in ['+','-','*','/']:
        		op2 = value.pop()
        		op1 = value.pop()
        		if token == '+':
        			value.append(op1 + op2)
        		elif token == '-':
        			value.append(op1 - op2)
        		elif token == '*':
        			value.append(op1 * op2)
        		elif token == '/':
        			if op1 < 0 and op2 > 0 or op1 > 0 and op2 < 0:
        				temp = abs(op1) / abs(op2)
        				value.append(-temp)
        			else:
        				value.append(op1/op2)
        			#print op1,op2,token,op1/op2,value[-1]
        	else:
        		value.append(int(token))
        return value.pop()
tks = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] #["4", "13", "5", "/", "+"] # ["2", "1", "+", "3", "*"]
s = Solution()
print s.evalRPN(tks)