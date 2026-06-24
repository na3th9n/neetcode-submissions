class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        if (nums.length === 0) {
            return false;
        }

        const n = new Set();

        for (let i = 0; i < nums.length; i++) {
            if (n.has(nums[i])) {
                return true;
            }

            n.add(nums[i]);
        }

        return false;

        // create a set and if the element is already within the set, return true
        // loop through the array 
    }
}
