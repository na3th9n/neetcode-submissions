class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b);
        const res = new Set();

        for (let i = 0; i < nums.length - 2; i++) {
            for (let j = i + 1; j < nums.length - 1; j++) {
                for (let k = j + 1; k < nums.length; k++) {
                    if (nums[i] + nums[j] + nums[k] === 0) {
                        const key = JSON.stringify([nums[i], nums[j], nums[k]]);
                        res.add(key);
                    }
                }
                
            }
        }

        return Array.from(res).map((item) => JSON.parse(item));
    }
}
