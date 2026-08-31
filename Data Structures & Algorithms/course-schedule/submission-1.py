class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p_map = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            p_map[c].append(p)

        seen = set()

        def dfs(c, seen):
            if c in seen:
                return False

            if p_map[c] == []:
                return True

            seen.add(c)

            for p in p_map[c]:
                if not dfs(p, seen):
                    return False

            seen.remove(c)
            p_map[c] = []
            
            return True

        for c in range(numCourses):
            if not dfs(c, seen):
                return False

        return True 

        