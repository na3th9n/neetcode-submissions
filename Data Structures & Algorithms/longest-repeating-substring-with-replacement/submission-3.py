class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # size of the window (r - l + 1) - maxf <= k
        # find the maximum 
        res = 0
        count = {}

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(count.values())

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                max_freq = max(count.values())
                l += 1

            res = max(res, r - l + 1)

        return res


        


               
          
         
                
        

        