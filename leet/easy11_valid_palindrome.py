class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = s.lower()
        alpha = []
        for char in normalized:
            if char not in "abcdefghijklmnopqrstuvwxyz1234567890":
                continue
            alpha.append(char)
        normalized = "".join(alpha)
        return normalized == "".join(list(reversed(normalized)))