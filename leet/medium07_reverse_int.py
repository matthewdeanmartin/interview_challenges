class Solution:
    def reverse(self, x: int) -> int:
        as_str = str(x)
        is_negative = False
        if "-" in as_str:
            as_str = as_str.replace('-','')
            is_negative=True

        the_reverse = int("".join(list(reversed(as_str))))
        if is_negative:
            the_reverse *= -1

        if the_reverse < -(2**31):
            return 0
        if the_reverse > (2**31) - 1:
            return 0
        return the_reverse