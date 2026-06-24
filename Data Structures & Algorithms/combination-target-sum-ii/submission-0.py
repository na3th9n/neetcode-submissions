class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def find_combo_sum(i, curr_target, curr_combo):
            if curr_target == 0:
                res.add(tuple(curr_combo))
                return

            if curr_target < 0 or i >= len(candidates):
                return

            # include current candidate
            curr_combo.append(candidates[i])
            find_combo_sum(i + 1, curr_target - candidates[i], curr_combo)
            curr_combo.pop()
            
            # exclude candidate
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            find_combo_sum(i + 1, curr_target, curr_combo)
            
            return

        find_combo_sum(0, target, [])

        return [list(combo) for combo in res]
            