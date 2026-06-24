class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 can not be greater than s2

        if len(s1) > len(s2):
            return False

        # init the arrays
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # iterate through both arrays once
        matches = 0

        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            # adding next item into window
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1

            if s1_count[index] == s2_count[index]:
                matches += 1

            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            # decrement previous item from window
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1

            if s1_count[index] == s2_count[index]:
                matches += 1

            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            l += 1

        return matches == 26

            
        
