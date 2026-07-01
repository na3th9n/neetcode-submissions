class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        const match = {
            ')': '(',
            ']': '[',
            '}': '{',
        };

        for (let b of s) {
            if (b === '(' || b === '[' || b === '{') {
                stack.push(b);
            } else {
                const openB = stack.pop();
                if (match[b] !== openB) {
                    return false;
                }
            }
        }

        return stack.length === 0;
    }
}
