class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                required = -(nums[i] + nums[j])
                left = j + 1
                right = n - 1
                while (left <= right):
                    mid = left + (right - left) // 2
                    if required == nums[mid]:
                        res.append((nums[i], nums[j], required))
                        break
                    elif required < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
        return [list(triplet) for triplet in res]