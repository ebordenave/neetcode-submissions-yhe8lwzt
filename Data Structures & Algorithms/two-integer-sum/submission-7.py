class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # prev map
      prevMap = {}

      for idx, num in enumerate(nums):
    
        diff = target - num

        if diff in prevMap.keys():
          return [prevMap[diff], idx]

        prevMap[num] = idx

      # iterate through nums tracking pos, num
        # create a compliment

        # if that compliment is in the prevMap
          # return the indices of where this number and its compliment are position

        # else is implied here
        # add the current number and its index into the prev map


        