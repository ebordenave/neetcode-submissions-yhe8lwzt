class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def count_char(word: str):
            cnt = {}
            for char in word:
                if char in cnt:
                    cnt[char] += 1
                else:
                    cnt[char] = 1

            return cnt
        
        return count_char(s) == count_char(t)

        