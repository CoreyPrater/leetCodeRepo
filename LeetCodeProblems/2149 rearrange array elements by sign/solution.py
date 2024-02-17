class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [y for y in nums if y < 0]
        result = []
  
        for item1, item2 in zip(pos, neg):
            result.append(item1)
            result.append(item2)
  
        return result