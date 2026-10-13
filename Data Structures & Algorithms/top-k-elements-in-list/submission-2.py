class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1;

        # arr = [(freq, num) for num, freq in count.items()]
        # arr.sort(reverse = True)

        # return [num for freq, num in arr[:k]]

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        

