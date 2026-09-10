class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = {i: [] for i in range(n)}
        visited = set()

        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)
        
        def dfs(curr, prev):
            if curr in visited:
                return False

            visited.add(curr)

            for neighbor in adj_map[curr]:
                if neighbor == prev:
                    continue

                if not dfs(neighbor, curr):
                    return False

            return True
            
        if dfs(0, -1) and len(visited) == n:
            return True
        else:
            return False
        