class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop()+stack.pop())
            elif token == '-':
                stack.append(-stack.pop()+stack.pop())
            elif token == '*':
                stack.append(stack.pop()*stack.pop())
            elif token == '/':
                val1,val2 = stack.pop(), stack.pop()
                if val2 / val1 > 0:
                    stack.append(val2//val1)
                else:
                    stack.append(math.ceil(val2/val1))
            else:
                stack.append(int(token))
        
        return stack.pop()
