class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // create a hash for both strings
        // if the hashs are equal together, they are anagram
        // O(n) time to loop through each string and count the letters
        // if the strings are not the same length, we know they are not anagrams of each other
        // O(nlogn) if we sorted both strings and use a loop to check each character of the string to see if they match
        
        if (s.length !== t.length) {
            return false
        }

        const s_hash = {};
        const t_hash = {};

        for (let i = 0; i < s.length; i++) {
           s_hash[s[i]] = (s_hash[s[i]] ?? 0) + 1; 
           t_hash[t[i]] = (t_hash[t[i]] ?? 0) + 1; 
        }

        for (const key in s_hash) {
            if (s_hash[key] !== t_hash[key]) {
                return false
            }
        }

        return true
    }
}
