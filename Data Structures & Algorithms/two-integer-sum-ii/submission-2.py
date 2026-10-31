class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in seen:
                return [seen[complement], i + 1]
            seen[numbers[i]] =  i + 1
        return []