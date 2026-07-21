class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        // need an index i to tell which index of nums we are considering
        // pass down the current subset
        // use recursive dfs to build each subset
        
        // base case: if i > nums.length, 
        // recursive calls: 2 calls, one includes the current index and one does not. Both pointers still move but the subset changes
        // return: nothing
            // have a global result res array to hold all the subsets

        const res = [];

        const dfs = (i, subset) => {
            if (i >= nums.length) {
                res.push([...subset]);
                return;
            }

            subset.push(nums[i]);
            dfs(i + 1, subset);
            subset.pop();
            dfs(i + 1, subset);

            return;
        }

        dfs(0, []);

        return res;
    }
}
