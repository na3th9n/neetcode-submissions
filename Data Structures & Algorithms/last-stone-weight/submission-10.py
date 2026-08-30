from heapq import heappop, heappush, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)
            diff = first - second

            if diff != 0:
                heappush(stones, diff)

        return 0 if len(stones) == 0 else abs(stones[0])
