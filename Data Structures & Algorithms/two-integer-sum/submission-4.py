class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_seen = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in prev_seen:
                return [prev_seen[complement], idx]

            prev_seen[num] = idx