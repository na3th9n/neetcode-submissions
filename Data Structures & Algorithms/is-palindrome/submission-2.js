class Solution {
    /**
     * @param {char} c 
     * @return {boolean}
     */
    isAlphaNum(c) {
        return (
            ('A' <= c && c <= 'Z') ||
            ('a' <= c && c <= 'z') ||
            ('0' <= c && c <= '9')
        );
    }
    
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0
        let r = s.length - 1

        while (l < r) {
            while (l < r && !this.isAlphaNum(s[l])) {
                l++;
            }

            while (l < r && !this.isAlphaNum(s[r])) {
                r--;
            }

            if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
