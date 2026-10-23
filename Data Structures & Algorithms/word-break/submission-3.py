class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom-up dp (cache)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            print(i)
            for word in wordDict:
                n = len(word)

                if i + len(word) <= len(s) and word == s[i:i+n]:
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break

        return dp[0]
