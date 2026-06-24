class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        
        for i in range(size):
            for j in range(i+1, size):
                if temperatures[i] < temperatures[j]:
                    res[i] = j - i
                    break

        return res
        