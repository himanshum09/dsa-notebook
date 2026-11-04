class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                required = -(nums[j] + nums[i])
                if required in seen:
                    res.add((nums[i], nums[j], required))
                
                seen.add(nums[j])
        return [list(triplet) for triplet in res]