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
        console.log(s_sort, t_sort);

        for (let i = 0; i < s.length; i++) {
            console.log(s_sort[i], t_sort[i]);
            if (s_sort[i] !== t_sort[i]) {
                return false;
            }
        }

        return true;
    }
}
