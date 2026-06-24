class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            # cleanse data
            s_new = "".join(sorted([c.lower() for c in s if s.isalnum()]))

            if s_new not in res:
                res[s_new] = [s]
            else:
                res[s_new].append(s)

        return list(res.values())
            

