class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def count(word):

            count = {}

            for ch in word:
                count[ch] = 1 + count.get(ch, 0)

            return count

        return count(s) == count(t)
        