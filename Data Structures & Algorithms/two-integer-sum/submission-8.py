class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prevSeen = {}
      
      for idx, num in enumerate(nums):
        diff = target - num
        
        if diff in prevSeen.keys():
          return [prevSeen[diff], idx]
        
        prevSeen[num] = idx        