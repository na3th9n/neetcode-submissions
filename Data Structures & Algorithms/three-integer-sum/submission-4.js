class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        // if brute force is O(n^3), we might as well sort the array to non-decreasing order
        // want unique combinations so we start iterating through the array and skipping any duplicates on the current index
        // since sorted, we can run two pointer to find a solution
        // same idea within the 2 pointer, to remove any duplicate combinations, if decrementing a pointer
        // keep incrementing/decrementing until a new value appears

        nums.sort((a, b) => a - b);

        let first = 0;
        const res = [];

        while (first < nums.length - 2) {
            let second = first + 1;
            let third = nums.length - 1;

            while (second < third) {
                const target = -nums[first];
                const sum = nums[second] + nums[third];
                
                if (sum < target) {
                    second += 1;
                } else if (sum > target) {
                    third -= 1;
                } else {
                    res.push([nums[first], nums[second], nums[third]]);
                    second += 1;
                    third -= 1;
                    while (second < third && nums[second] == nums[second - 1]) second += 1;
                    while (second < third && nums[third] == nums[third + 1]) third -= 1;
                }
            }
            first += 1;
            while (first < nums.length - 2 && nums[first] == nums[first - 1]) first += 1;
        }

        return res;
    }
}