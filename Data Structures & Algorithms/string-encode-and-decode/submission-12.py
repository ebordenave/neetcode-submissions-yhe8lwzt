class Solution:

    def encode(self, strs: List[str]) -> str:
      encoded = ""

      for word in strs:
        encoded += str(len(word)) + "#" + word

      return encoded

    def decode(self, s: str) -> List[str]:
      i, res = 0, []

      while i < len(s):
        sep = i

        while s[sep] != "#":
          sep += 1

        length = int(s[i:sep])

        word_start = sep + 1
        word_end = word_start + length
        i = word_end
        res.append(s[word_start:word_end])

      return res


