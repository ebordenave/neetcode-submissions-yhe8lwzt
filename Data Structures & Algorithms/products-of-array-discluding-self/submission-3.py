class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      res = [1] * len(nums) # print [1,1,1,1]
      # print(res)

      prefix = 1

      for i in range(len(nums)): # left to right traversal
        res[i] = prefix 
        prefix *= nums[i]

      postfix = 1

      for i in range(len(nums)-1, -1, -1): # traverse from left to right
        res[i] *= postfix
        postfix *= nums[i]

      return res