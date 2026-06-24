class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"}" : "{", ")" : "(", "]" : "["}

        for b in s:
            match b:
                case "}" | "]" | ")":
                    print("hi")
                    if stack and matches[b] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                case _:
                    stack.append(b)

        return not stack