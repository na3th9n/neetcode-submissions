class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        # what array are we searching?
        # what are the conditions to move the left or right pointer

        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)


            if hours <= h:
                res = min(res, k)
                r = k - 1
            elif hours > h: 
                l = k + 1

        return res
