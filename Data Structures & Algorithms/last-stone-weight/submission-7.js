class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        stones.sort((a, b) => a - b);
        console.log(stones);

        while (stones.length > 1) {
            const first = stones.pop();
            const second = stones.pop();

            if (first !== second) {
                stones.push(first - second);
                stones.sort((a, b) => a - b);
            }
            console.log(stones);
        }

        return stones.length >= 1 ? stones[0] : 0;
    }
}
