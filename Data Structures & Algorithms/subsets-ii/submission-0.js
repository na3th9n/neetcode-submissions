class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        const res = [];
        nums.sort((a, b) => a - b);

        const dfs = (i, subset) => {
            if (i >= nums.length) {
                res.push([...subset]);
                return;
            }

            subset.push(nums[i]);
            dfs(i + 1, subset);
            subset.pop();

            while (i + 1 < nums.length && nums[i + 1] === nums[i] ) {
                i++;
            }
            
            dfs(i + 1, subset);

            return;
        };

        dfs(0, []);

        return res;
    }
}
