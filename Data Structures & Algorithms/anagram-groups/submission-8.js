class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // to check if 2 anagrams are the same, you can create two hashes for each string and then compare each key together
        // create a hash for each string
        // sort each string 

        // do a loop that saves a copy of the sorted string, checks a hash if it exists, if it does exist, add it to an array, and if it doesn't, create a new key-value pair

        const strsHash = {}; 

        for (const s of strs) {
            const sortedS = s.split('').sort().join('');

            if (!strsHash[sortedS]) {
                strsHash[sortedS] = [];
            }

            strsHash[sortedS].push(s);
        }
        
        return Object.values(strsHash);
    }
}
