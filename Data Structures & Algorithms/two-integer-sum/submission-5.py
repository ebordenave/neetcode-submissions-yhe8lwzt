class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prevMap = {} # val : index
      
      for idx, num in enumerate(nums):
        # print(idx, num)
        diff = target - num # calculates the complement
        
        if diff in prevMap: # check if the difference is in the hashmap (this confirms the second num required to calculcate the sum)
          return [prevMap[diff], idx] # if it is, return the position of the difference val, and the pos of the first number. These positions tell us where the values that equal the sum
        prevMap[num] = idx # ELSE take the current num and place it into the hashmap based on the index