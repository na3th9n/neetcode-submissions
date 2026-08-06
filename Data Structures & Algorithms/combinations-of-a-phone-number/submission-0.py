class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = "" 
        digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return res

        def dfs(i, letters):
            if i >= len(digits):
                res.append(letters)
                return 

            # recursively call each letter associated with the digit
            for c in digits_to_letters[digits[i]]:
                letters += c
                dfs(i + 1, letters)
                letters = letters[:-1]

            return

        dfs(0, letters)
        return res
        

            
        