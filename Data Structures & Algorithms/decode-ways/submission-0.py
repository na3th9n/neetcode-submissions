class Solution:
    def numDecodings(self, s: str) -> int:
        # recurrsive relationship = dfs(i) = dfs(i + 1) + dfs(i + 2)
        # use the i pointer as the state the answer inside
        # base case: empty string = 1 or when the i pointer reaches the len(s) index which is out of bounds or empty string
        # edge case: if i == 0, return 0
            # 011 returns 0
            # 101, we will explore 1 and 10 but once we go down 1 path, and we explore 0 and 01, those paths would be pruned

        dp = { len(s) : 1 }

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and 0 < int(s[i:i+2]) <= 26:
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)



