class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        

        n = 9

        sb = {i: [] for i in range(n)}
        row = {i: [] for i in range(n)}
        col = {i: [] for i in range(n)}


        for i in range(n): # row
            for j in range(n): # column
                if board[i][j].isdigit():
                    num = int(board[i][j])

                    if num in row[i]:
                        return False
                    else:
                        row[i].append(num)

                    if num in col[j]:
                        return False

                    else:
                        col[j].append(num)

                    sb_index = (i // 3) * 3 + (j // 3)

                    if num in sb[sb_index]:
                        return False
                    else:
                        sb[sb_index].append(num)

        return True

        