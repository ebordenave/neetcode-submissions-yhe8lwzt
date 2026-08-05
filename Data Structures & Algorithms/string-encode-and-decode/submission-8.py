class Solution:

    def encode(self, strs: List[str]) -> str:
      encoded = ""

      for word in strs:
        encoded += str(len(word)) + "#" + word

      return encoded

    def decode(self, s: str) -> List[str]:
      res, i = [], 0

      while i < len(s):
        j = i

        while s[j] != "#":

          j += 1
          # for me the core of the algorithm is here
          # I don't fully understand what is happening
          # This is the part I need to make a mental model
          # of. What would help is some comments that show
          # where the pointers, what they are doing relative
          # to the string
        length = int(s[i:j])
        i = j + 1
        
        j = i + length
        res.append(s[i:j])
        i = j

      return res

