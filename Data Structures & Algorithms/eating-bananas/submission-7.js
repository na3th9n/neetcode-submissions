class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let l = 1,
            r = Math.max(...piles);
        let res = r;

        const eat = (k) => {
            let timeToEat = 0;

            for (const p of piles) {
                timeToEat += Math.ceil(p / k);
            }

            return timeToEat;
        };

        while (l <= r) {
            const k = Math.floor((l + r) / 2);
            const timeToEat = eat(k);

            if (timeToEat <= h) {
                res = Math.min(res, k);
                r = k - 1;
            } else {
                l = k + 1;
            }

        }

        return res;
    }
}
