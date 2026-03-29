class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # intitialize and declare a set called numsSet
        # this will contain all the unique values of num
        numsSet = set(nums)

        return len(nums) != len(numsSet)

        # return if len(nums) != set.size() return True
        # there is duplicate
        # the reason is if nums contains [1,2,2,3] its length is equal to 4
        # the set version of nums would equal 3 because there are only 3
        # unique values. If the nums and setnums are not equals, it confirms
        # that nums does contain a duplicate


         