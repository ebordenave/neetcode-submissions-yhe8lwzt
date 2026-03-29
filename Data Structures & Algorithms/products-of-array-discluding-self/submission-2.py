class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      # create an arr equal to len(nums) where each slot has a value of 1
      res = [1] * len(nums)
      # initialize my prefix var SET to 1
      prefix = 1
        
      # loop through len(nums) using i and multiply i and the prefix traversing from left to right
      for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        
      postfix = 1
      
      for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        
      return res
        