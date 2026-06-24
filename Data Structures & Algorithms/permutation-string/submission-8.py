class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map, s2_map = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord("a")] += 1
            s2_map[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            indexL = ord(s2[l]) - ord("a")
            indexR = ord(s2[r]) - ord("a")
            s2_map[indexR] += 1

            if s1_map[indexR] == s2_map[indexR]:
                matches += 1
            elif s1_map[indexR] + 1 == s2_map[indexR]:
                matches -= 1

            s2_map[indexL] -= 1

            if s1_map[indexL] == s2_map[indexL]:
                matches += 1
            elif s1_map[indexL] - 1 == s2_map[indexL]:
                matches -= 1
            
            l += 1
        
        return matches == 26

        

        