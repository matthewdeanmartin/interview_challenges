from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hist = {}
        for num in nums:
            so_far = hist.get(num)
            if so_far:
                hist[num] +=1
            else:
                hist[num] =1
        for key, value in hist.items():
            if value ==1:
                return key
        # shouldn't get here.

assert Solution().singleNumber([1,1,2]) ==2
assert Solution().singleNumber([3, 1,1,2,2]) ==3