class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use dfs to solve the problem
        # base case:
            # if adjacent cells do not give the desired work: return false
            # if adjacent cells have the last letter: return true
        # state:
            # pointer to the next letter of word
        
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])
        word_size = len(word)


        def dfs(r: int, c: int, k: int) -> bool:
            if board[r][c] != word[k]:
                return False

            if k == word_size - 1:
                return True

            tmp = board[r][c]
            board[r][c] = "#"

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    if dfs(nr, nc, k + 1):
                        board[r][c] = tmp
                        return True

            board[r][c] = tmp
            return False

        for i in range(rows):
            for j in range(cols):
                cell = board[i][j]
                if dfs(i, j, 0):
                    return True

        return False

