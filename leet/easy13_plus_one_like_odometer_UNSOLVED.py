from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # handle general case
        digits[-1] = digits[-1] + 1
        print(digits)
        carry = 0
        for i, digit in enumerate(reversed(digits)):
            digits[i] = digits[i] + carry
            print(digits)
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
        if carry:
            digits = [1] + digits
        return digits

assert Solution().plusOne([1]) ==[2]
assert Solution().plusOne([1,2,3]) ==[1,2,4]
assert Solution().plusOne([9]) ==[1,0]
assert Solution().plusOne([9,9]) ==[1,0,0]



