class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack
        stack = []
        close_to_open = {")":"(", "]":"[", "}":"{"}

        for b in s:
            if b in close_to_open:
                if stack and stack[-1] == close_to_open[b]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(b)
                

        return not stack