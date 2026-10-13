class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // brute-force
        // for (let i = 0; i < nums.length; i++) {
        //     for (let j = i + 1; j < nums.length; j++) {
        //         if (nums[j] === nums[i]) return true;
        //     }
        // }
        // return false;

        // 2 x O(n)
        // one for set and one for array spread
        // return !([...new Set(nums)].length === nums.length);

        const seen = new Set();
        for (const num of nums) {
            if (seen.has(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
