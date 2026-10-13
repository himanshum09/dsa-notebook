class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // brute force
        // for (let i = 0; i < nums.length; i++) {
        //     for (let j = i + 1; j < nums.length; j++) {
        //         if (nums[i] + nums[j] === target) return [i, j];
        //     }
        // }
        // return [];

        // sorting
        // let arr = [];
        // for (let i = 0; i < nums.length; i++) {
        //     arr.push([nums[i], i]);
        // }

        // arr.sort((a, b) => a[0] - b[0]);

        // let i = 0, j = nums.length - 1;

        // while (i < j) {
        //     let curr = arr[i][0] + arr[j][0];
        //     if (curr === target) {
        //         return [Math.min(arr[i][1], arr[j][1]), Math.max(arr[i][1], arr[j][1])];
        //     } else if (curr < target) {
        //         i++;
        //     } else {
        //         j--;
        //     }
        // }
        // return [];

        // Hash Map - 1 (two pass)
        // const indices = {};

        // for (let i = 0; i < nums.length; i++) {
        //     indices[nums[i]] = i // val -> index
        // }

        // for (let i = 0; i < nums.length; i++) {
        //     const diff = target - nums[i];
        //     if (indices[diff] !== undefined && indices[diff] !== i) {
        //         return [i, indices[diff]];
        //     }
        // }
        // return [];

        const valueToIndex = new Map();

        for (let i = 0; i < nums.length; i++) {
            const diff = target - nums[i];
            if (valueToIndex.has(diff)) {
                return [valueToIndex.get(diff), i];
            }

            valueToIndex.set(nums[i], i)
        }
        return [];
    }
}
