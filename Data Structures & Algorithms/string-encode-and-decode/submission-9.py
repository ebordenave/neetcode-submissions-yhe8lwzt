class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, encoded: str) -> List[str]:
        words = []
        i = 0

        while i < len(encoded):
            separator = i

            # Find the delimiter
            while encoded[separator] != "#":
                separator += 1

            # Now we're past the delimiter, so parse the word
            length = int(encoded[i:separator])
            word_start = separator + 1
            word_end = word_start + length

            words.append(encoded[word_start:word_end])
            i = word_end

        return words