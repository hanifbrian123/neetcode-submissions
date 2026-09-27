class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []
        operators = "+-*/"
        def compute(a, b, op):
            if op == "+": return a+b
            elif op == "-": return a-b
            elif op == "*": return a*b
            elif op == "/": return a/b
        for t in tokens:
            if t in operators:
                b = int(operandStack.pop())
                a = int(operandStack.pop())
                operandStack.append(str(compute(a, b, t)))
            else:
                operandStack.append(t)
        return int(operandStack[0])
