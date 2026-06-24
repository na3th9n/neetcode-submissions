class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            match b:
                case ")": 
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                case "}": 
                    if stack and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                case "]":
                    if stack and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                case _:
                    stack.append(b)

        return not stack