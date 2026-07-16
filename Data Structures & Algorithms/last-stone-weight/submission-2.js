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

            maxHeap.enqueue(-(x - y));
        }

        return maxHeap.size() === 1 ? -maxHeap.front() : 0;
    }
}
