class Solution:

    def encode(self, strs: List[str]) -> str:
      encoded = ""

      for word in strs:
        encoded += str(len(word)) + "#" + word

      return encoded

    def decode(self, s: str) -> List[str]:
      i, res = 0, []

      while i < len(s):
        separator = i

        while s[separator] != "#":
          separator += 1

        length = int(s[i:separator])
        word_start = separator + 1
        word_end = word_start + length
        res.append(s[word_start:word_end])
        i = word_end

      return res
