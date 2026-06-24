class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        if (!nums.length) {
            return false
        }

        for (let i = 0; i < nums.length - 1; i++) {
            for (let j = i + 1; j < nums.length; j++) {
                // console.log(i);
                // console.log(j);
                if (nums[i] === nums[j]) {
                    return true
                }
            }
        }

        return false
    }
}
