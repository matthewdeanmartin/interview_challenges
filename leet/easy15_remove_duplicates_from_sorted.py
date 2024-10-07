from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # remove dupes, preserve order
        # returns number of unique elements
        # items = len(nums)
        # unique = []
        # for i, num in enumerate(nums):
        #     if num

        # check if shortcut works.
        # works but isn't efficient.
        nums_sort = list(nums)
        uniques = list(set(nums))
        nums.clear()
        # nums.extend(uniques)
        for i in nums_sort:
            if i in uniques and i not in nums:
                nums.append(i)

        return len(nums)

# TODO: missing asserts against nums.
assert Solution().removeDuplicates([1,1,1]) ==1
assert Solution().removeDuplicates([-1,0,0,0,0,3])==3
assert Solution().removeDuplicates([3,0,0,0,0,-1])==3