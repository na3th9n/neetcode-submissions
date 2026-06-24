class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = {}
        bucket_sort = [[] for _ in range(len(nums))]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for num, freq in count.items():
            bucket_sort[freq - 1].append(num)

        res = []

        times = 0
        for i in range(len(nums) - 1, -1, -1):
            for num in bucket_sort[i]:
                res.append(num)

                if len(res) == k:
                    return res

        return res