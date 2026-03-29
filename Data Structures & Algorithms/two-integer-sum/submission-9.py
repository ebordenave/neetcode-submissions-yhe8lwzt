class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prev_seen = {}

      for idx, num in enumerate(nums):
        diff = target - num

        if diff in prev_seen:
          return [prev_seen[diff], idx]

        prev_seen[num] = idx
        
        