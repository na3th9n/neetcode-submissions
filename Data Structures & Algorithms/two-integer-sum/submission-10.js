class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // key: num value, value: index

        const seen = new Map(); 
        
        for (let i = 0; i < nums.length; i++) {
            if (seen.has(target - nums[i])) {
                return [seen.get(target-nums[i]), i]; //might have to use .get()
            }

            seen.set(nums[i], i);
        }

        return [0, 0];
    }
}
