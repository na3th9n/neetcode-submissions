class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        const maxHeap = new MinPriorityQueue();

        for (const stone of stones) {
            maxHeap.enqueue(-stone);
        }

        // console.log(stones)
        // console.log(maxHeap);

        while (maxHeap.size() > 1) {
            const x = -maxHeap.dequeue();
            const y = -maxHeap.dequeue();
            console.log(x, y);
            // console.log(maxHeap);
            if (x === y) continue;

            const remaining = x - y;

            if (remaining > 0) {
                maxHeap.enqueue(-remaining);
            } 
        }

        if (maxHeap.size() === 0) {
            return 0
        }

        return -maxHeap.front();
    }
}
