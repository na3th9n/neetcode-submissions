class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        while (stones.length > 1) {
            stones.sort((a, b) => a - b);

            const first = stones.pop();
            const second = stones.pop();

            if (first !== second) {
                stones.push(first - second);
            }
        }

        return stones.length >= 1 ? stones[0] : 0;
    }
}
