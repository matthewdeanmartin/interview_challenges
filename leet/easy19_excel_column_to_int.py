class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # print(26^0)
        # This is the 'no google' solution.
        # I forgot how to conver char to ascii
        alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
        # Also for got instr for python
        translation = {}
        i = 1
        for char in alphabet:
            translation[char] = i
            i += 1
        # print(translation)
        # print("---------")
        # number = 0
        # place = 0
        # for column in reversed(columnTitle):
        #     print(column, translation[column], translation[column]*25^2,translation[column]*25^3)
        #     if place == 0:
        #         # just value
        #         number += translation[column]
        #     elif place == 1:
        #         number +=  (translation[column])*(25^2)
        #     else:
        #         number +=  translation[column]*(25^place) -1
        #     place += 1

        # 123 = 1 * 10^2 + 2 * 10^1 +  3 * 10^0
        # ZY = Z * 26^2 + Y * 26^1

        number = 0
        place = 0
        base = 26
        for column in reversed(columnTitle):
            digit_value = translation[column]
            if place == 0:
                number += digit_value
            else:
                # print(base^place) What was this?! It was bitwise or!
                number += (digit_value * pow(base, place))
            place += 1
        return number

assert Solution().titleToNumber("ZY")==701
