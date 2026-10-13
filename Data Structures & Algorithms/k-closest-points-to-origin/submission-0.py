import heapq
import math

# output has to be an array of the k cloest points
# sorting within the heap has to be based on the Euclidean distance
# so if we heappop() (k times) -> [x, y] but sort based on the Euclidean distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            dist = math.sqrt((x ** 2) + (y ** 2))
            minHeap.append((dist, x, y))

        heapq.heapify(minHeap)

        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res


        