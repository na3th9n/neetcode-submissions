from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        
        s_size = len(s)
        t_size = len(t)

        if s_size != t_size:
            return False

        for i in range(s_size):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1

        for i in range(len(count)):
            if count[i] != 0:
                return False

        return True


        