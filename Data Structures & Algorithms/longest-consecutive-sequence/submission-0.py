class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # initialize a set that will store each number seen in nums
        numsSet = set(nums)
        # init a longest var SET to 0
        longest = 0

        # iterate through the num set
        for num in numsSet:
            # if the current num minus 1 (prev num) is NOT in the set 
            if (num - 1) not in numsSet:
            # this means we're seeing the smallest number for the first time
                # init a var called length and SET it to 1
                length = 1

                # WHILE this current num + length is in nums set: (this means we are seeing a consecutive number)
                while (num + length) in numsSet:
                    # add 1 to our length
                    length += 1

                # SET longest var to the max value between longest and length
                longest = max(length, longest)
        # RETURN the longest
        return longest
        