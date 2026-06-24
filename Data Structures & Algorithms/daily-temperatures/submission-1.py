class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                currI, currT = stack.pop()
                res[currI] = i - currI
            
            stack.append([i, t])

        return res