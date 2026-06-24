class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(openB, closeB):
            if openB == closeB == n:
                res.append("".join(stack))
                return

            if openB < n:
                stack.append("(")
                backtracking(openB + 1, closeB)
                stack.pop()

            if closeB < openB:
                stack.append(")")
                backtracking(openB, closeB + 1)
                stack.pop()

        backtracking(0, 0)

        return res


        
        