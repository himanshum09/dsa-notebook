class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // brute force
        // const res = {};
        // for (let s of strs) {
        //     const sortedS = s.split('').sort().join('');
        //     if (!res[sortedS]) {
        //         res[sortedS] = []
        //     }
        //     res[sortedS].push(s)
        // }
        // return Object.values(res);

        const res = {};
        for (let s of strs) {
            const count = new Int32Array(26);
            for (let c of s) {
                const base = 'a'.charCodeAt(0);
                count[c.charCodeAt(0) - base] += 1;
            }
            const key = count.join(',');
            if (!res[key]) {
                res[key] = [];
            }
            res[key].push(s);
        }
        return Object.values(res);
    }
}
