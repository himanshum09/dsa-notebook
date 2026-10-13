class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // Sorting
        // const sortedS = s.split('').sort().join('');
        // const sortedT = t.split('').sort().join('');

        // return sortedS === sortedT;

        // Hash Map
        // if (s.length !== t.length) return false;

        // const countS = {};
        // const countT = {};

        // for (let i = 0; i < s.length; i++) {
        //     countS[s[i]] = (countS[s[i]] ?? 0) + 1;
        //     countT[t[i]] = (countT[t[i]] ?? 0) + 1;
        // }

        // for (const key in countS) {
        //     if (countS[key] !== countT[key]) return false
        // }
        // return true;
        
        // hash map with array
        if (s.length !== t.length) return false;

        const charArr = new Array(26).fill(0); // index in alphabet chars and value is frequency

        for (let i = 0; i < s.length; i++) {
            charArr[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            charArr[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }
        return charArr.every(char => char === 0);

    }
}
