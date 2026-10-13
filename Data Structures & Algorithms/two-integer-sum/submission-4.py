class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # arr: list[tuple[int, int]] = []
        # for i in range(len(nums)):
        #     arr.append((nums[i], i))
        
        # arr.sort(key= lambda x: x[0])

        # i, j = 0, len(nums) - 1;

        # while (i < j):
        #     curr = arr[i][0] + arr[j][0]
        #     if curr == target:
        #         idx1 = arr[i][1]
        #         idx2 = arr[j][1]
        #         return[min(idx1, idx2), max(idx1, idx2)]
        #     elif curr < target:
        #         i += 1;
        #     else:
        #         j -= 1;
        
        # return [];

        indices: dict[int, int] = {}

        for i, num in enumerate(nums):
            indices[num] = i
        
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        
        return []