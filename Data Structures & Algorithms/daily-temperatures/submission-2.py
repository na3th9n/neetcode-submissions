class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # the last iteration of the input array , we don't need to check
        # [2, 1, 1, 1, 4, 1, 1, ,1]
        # [1, 4]
        # [4]
        # stack = [2, 1, 1, 1,]
        # j - i 

        res = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            if stack:
                while stack and n > stack[-1][1]:
                    j = stack.pop()[0]
                    res[j] += i - j
            
            stack.append((i, n))
            print(stack)
        return res

        