class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # only hold open brackets

        for b in s:
            if b == "[" or b == "(" or b == "{":
                stack.append(b)

            if stack:
                if stack[-1] == "[" and b == "]" or stack[-1] == "(" and b == ")" or stack[-1] == "{" and b == "}":
                    stack.pop()

            else:
                return False

        return True if not stack else False

