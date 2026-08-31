class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build our adjacency list
        course_map = {c: [] for c in range(numCourses)}

        for c, p in prerequisites:
            course_map[c].append(p) # {0: [], 1: [0], 2: []}

        # create our visited set 
        visited = set()
        cycle = set()
        res = []

        # dfs implementation
        def dfs(c):
            if c in cycle: # cycle detected
                return False

            if c in visited:
                return True

            cycle.add(c)

            for p in course_map[c]:
                if not dfs(p):
                    return False
                
            cycle.remove(c)
            visited.add(c)
            # course_map[c] = []
            res.append(c)

            return True

        # dfs call implementation
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res

        