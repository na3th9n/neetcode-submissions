class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom-up dp (cache)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            print(i)
            for word in wordDict:
                n = len(word)

                if word == s[i:i+n]:
                    if dp[i+len(word)]:
                        dp[i] = True

        return dp[0]

        # leetcode
        # [0]
