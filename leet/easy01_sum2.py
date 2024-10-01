class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # should check if 2+ nums!
        candidates = []
        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums):
                if i + j == target and index_i != index_j:
                    candidates.append([index_i, index_j])
        # Not safe!
        return candidates[0]

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    assert Solution().twoSum([2,7,11,15],9) == [0,1]
    assert Solution().twoSum([3, 2, 4], 6) ==[0,2]
    assert Solution().twoSum([3,3], 6) == [0,1]
