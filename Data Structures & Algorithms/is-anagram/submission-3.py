class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def count_char(word: str):
            cnt = defaultdict(int)

            for char in word:
                cnt[char] += 1

            return cnt
            
        print(count_char(s))
        print(count_char(t))
        
        return count_char(s) == count_char(t)
        