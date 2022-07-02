class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        # print(6 / (-132))
        
        for i in tokens:
            if i in '+-*/':
                a =  stk.pop()
                b = stk.pop()
                if i == '+':
                    stk.append(a + b)
                elif i == '-':
                    stk.append(b - a)
                elif i == '*':
                    stk.append(a * b)
                elif i == '/':
                    stk.append(int(b / a))
            else:
                stk.append(int(i))
            # print(stk)
                
        return stk.pop()