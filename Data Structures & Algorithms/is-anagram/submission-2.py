class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        
        s_size = len(s)
        t_size = len(t)

        if s_size != t_size:
            return False

        for i in range(s_size):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1

        return s_freq == t_freq


        