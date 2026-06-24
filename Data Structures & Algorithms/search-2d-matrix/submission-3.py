class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1

            while l <= r:
                m = (l + r) // 2

                if matrix[i][m] == target:
                    return True

                elif matrix[i][m] < target:
                    l = m + 1

                else:
                    r = m - 1

        return False