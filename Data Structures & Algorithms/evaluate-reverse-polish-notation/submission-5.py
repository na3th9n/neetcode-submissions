class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    x = stack.pop()
                    stack.append(stack.pop() - x)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    x = stack.pop()
                    stack.append(int(stack.pop() / x))
                case _:
                    stack.append(int(t))

        return stack[0]

        