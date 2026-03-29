class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a count hashmap
        count = {}

        # create a freq array filled with buckets
        freq = [[] for item in range(len(nums)+1)]

        #loop through nums
        for num in nums:
          count[num] = 1 + count.get(num, 0)

        for num, count in count.items():
          freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
          for num in freq[i]:
            res.append(num)
            if len(res) == k:
              return res
