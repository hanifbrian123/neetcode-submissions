class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []
        operators = "+-*/"
        def compute(a, b, op):
            if op == "+": return a+b
            elif op == "-": return a-b
            elif op == "*": return a*b
            elif op == "/": return int(a/b)
        for t in tokens:
            if t in operators:
                b = operandStack.pop()
                a = operandStack.pop()
                operandStack.append(compute(a, b, t))
            else:
                operandStack.append(int(t))

        return operandStack[0]
