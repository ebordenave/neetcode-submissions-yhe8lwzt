class Solution:
    def count_char(self, word: str):
        count = defaultdict(int)

        for char in word:
            count[char] += 1

        return count

    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_char(s) == self.count_char(t)
        