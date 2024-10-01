class Solution:
    def isPalindrome(self, x: int) -> bool:
        return "".join(reversed(str(x))) == str(x)