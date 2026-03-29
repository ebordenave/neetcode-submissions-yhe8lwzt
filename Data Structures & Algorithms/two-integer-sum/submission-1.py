class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize and declare a prevSeen hashmap
        prevSeen = {}
        # this will contain keys equal to the num in nums, and values
        # will be their index

        # iterate through nums, keeping track of nums and their indices
        for index, num in enumerate(nums):
        # for index, num in enumerate(nums):

        # initialize and declare a complement var SET to target - num
            complement = target - num
        # if that complement is in prevSeen hashmap
            if complement in prevSeen:
            # return a list [prevSeen[complement], index]
                return [prevSeen[complement], index]
        # otherwise prevSeen[num] = index
            prevSeen[num] = index