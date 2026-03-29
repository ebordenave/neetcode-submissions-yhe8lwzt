class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialize and declare a count dictionary

        # make a helper function that will return the count 
        # of each string input


        def count(s: str) -> dict:
            count = {}

            for char in s:
                if char not in count:
                    count[char] = 0
                count[char] += 1
            return count

        return count(s) == count(t)
        