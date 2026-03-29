class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      # initialize a count hashmap
      count = {}

      # create my buckets equal to len of nums + 1
      freq = [[] for i in range(len(nums) + 1)]

      # populate my hashmap such that it is value : frequency
      for num in nums:
        count[num] = 1 + count.get(num, 0)

      # iterate through the count hashmap items to populate freq
      for num, count in count.items():
        # freq count should have a value of the num appended to it (added to the freq bucket)
        freq[count].append(num)

      # create a res array
      res = []

      # tricky here but step through our freq array backwards
      for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
          res.append(n)

          if len(res) == k:
            return res