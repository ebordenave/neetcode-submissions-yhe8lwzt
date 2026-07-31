class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], idx] # not sure about this

            # otherwise
            seen[num] = idx

        return
        