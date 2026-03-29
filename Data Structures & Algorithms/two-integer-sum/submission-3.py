class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in prev_seen:
                return [prev_seen[complement], index]

            prev_seen[num] = index
        