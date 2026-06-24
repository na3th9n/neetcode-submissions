class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we use a stack to hold the state of the current made paranthesis 
        # we will either add a open or close
        # we will only add a open if it is less than n or >= close
        # we can only add close if it is less than open

        stack = []
        res = []

        def backtracking(open_n, close_n):
            if open_n == close_n == n:
                res.append("".join(stack))
                return 

            if open_n < n:
                stack.append("(")
                backtracking(open_n + 1, close_n)
                stack.pop()

            if close_n < open_n:
                stack.append(")")
                backtracking(open_n, close_n + 1)
                stack.pop()

        backtracking(0, 0)
        return res

