# return floor of square root w/o using square root function
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        best = 0
        error = 10000000000
        # brute force
        for i in range(1, x + 1):
            current_error = abs(x - (i * i))
            print(i, current_error)
            if current_error < error:
                best = i
                error = current_error
        # Edge cases?
        if best * best == x:
            return best
        if best == 1:
            return best
        # Nope, this doesn't work
        return best - 1



