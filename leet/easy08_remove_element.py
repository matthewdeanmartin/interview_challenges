from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two solutions one with mutation, one without
        result = []
        for num in nums:
            if num == val:
                continue
            else:
                result.append(num)
        # simulate immutable because assertion is on a reference to nums
        nums.clear()
        nums.extend(result)
        return len(nums)