class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1;

        arr = [(freq, num) for num, freq in count.items()]
        arr.sort(reverse = True)

        return [num for freq, num in arr[:k]]
