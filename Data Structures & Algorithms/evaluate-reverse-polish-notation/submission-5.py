class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for i in range(0, len(tokens)):
            n = tokens[i]
            if n == "+" or n == "-" or n == "*" or n == "/":
                b = operands.pop()
                a = operands.pop()
                c = 0
                if n == "*":
                    c = a * b
                elif n == "/": 
                    c = int(a / b)
                elif n == "+":
                    c = a + b
                elif n == "-":
                    c = a - b
                operands.append(c)
            else:
                operands.append(int(n))

        return operands.pop()

            