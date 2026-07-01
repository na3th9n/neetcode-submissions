class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        if (s.length === 0) {
            return 0;
        } 

        if (s.length === 1) {
            return 1
        }

        const seen = new Set();
        let l = 0;
        let res = 1;
        seen.add(s[l]);

        for (let r = 1; r < s.length; r++) {
            console.log(s[r], seen);
            while (seen.has(s[r])) {
                seen.delete(s[l]);
                console.log(s[l]);
                l++;
            }

            seen.add(s[r]);
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}
