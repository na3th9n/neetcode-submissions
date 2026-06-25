class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }

        let s_sort = s.split('').sort().join('');
        let t_sort = t.split('').sort().join('');

        return s_sort === t_sort;
    }
}
