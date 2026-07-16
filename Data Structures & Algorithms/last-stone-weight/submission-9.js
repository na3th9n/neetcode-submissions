class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        stones.sort((a, b) => a - b);

        while (stones.length > 1) {
            const first = stones.pop();
            const second = stones.pop();

            if (first !== second) {
                const n = stones.length + 1;
                let pos = 0;
                const diff = first - second;

                let l = 0;
                let r = stones.length;

                // find the index where we can insert the number
                while (l < r) {
                    let mid = Math.floor((l + r) / 2)

                    if (stones[mid] < diff) {
                        l = mid + 1;
                    } else {
                        r = mid;
                    } 
                }

                pos = r;
                stones.push(0);

                for (let i = n - 1; i > pos; i--) {
                    stones[i] = stones[i - 1]
                }

                stones[pos] = diff;
            }
        }

        return stones.length >= 1 ? stones[0] : 0;
    }
}
