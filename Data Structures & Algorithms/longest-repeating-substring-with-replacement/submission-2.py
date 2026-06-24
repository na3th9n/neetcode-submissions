class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # best possible case: you already have k number of same values 
        # and you just change the others to be the same character
        charCount = {}
        res = 0
        l = 0

        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1

            while (r - l + 1) - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
