class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        // one pointer will always iterate 
        // the left pointer will switch if the right pointer is smaller than it
        // 10 - 2 = 8
        // 3 - 1 = 2
        // you can just switch because you only have to save the amount of money

        if (prices.length == 1) {
            return 0;
        }

        let buy = 0;
        let res = 0;

        for (let sell = 1; sell < prices.length; sell++) {
            res = Math.max(res, prices[sell] - prices[buy]);

            if (prices[sell] < prices[buy]) {
                buy = sell;
            }
        }

        return res;
    }
}
