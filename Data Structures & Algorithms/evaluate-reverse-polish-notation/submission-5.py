class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch in ('+', '-', '*', '/'):
                # Always pop the right operand first, then the left operand
                b = stack.pop()
                a = stack.pop()
                
                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
                elif ch == '/':
                    # Standard truncation toward zero for RPN (e.g., LeetCode style)
                    stack.append(int(a / b))
            else:
                stack.append(int(ch))
                
        return stack[0]
