from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        
        s_size = len(s)
        t_size = len(t)

        if s_size != t_size:
            return False

        for i in range(s_size):
            s_freq[s[i]] += 1
            t_freq[t[i]] += 1

        return s_freq == t_freq


        