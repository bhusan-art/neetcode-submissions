class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [];
        operator = {'+' , '-' , '*' , '/' }

        for t in tokens:
            if t in operator:
                a =  stack.pop();
                b = stack.pop();
                if t == '+':
                    c = b + a
                elif t == '-':
                    c = b - a
                elif t == '*':
                    c = b * a
                else:               # t == '/'
                    c = int(b / a)
                stack.append(c);
            else:
                stack.append(int(t));
            
        return stack.pop()
                