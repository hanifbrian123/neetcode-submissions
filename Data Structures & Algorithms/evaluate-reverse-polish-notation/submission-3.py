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
                b = float(operandStack.pop())
                a = float(operandStack.pop())
                operandStack.append(int(compute(a, b, t)))
            else:
                operandStack.append(int(t))

        return operandStack[0]
