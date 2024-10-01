romans =  {
    'I':1,
    'II':2,
    'III':3,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
negatives = {
    "I": -1,
    "X": -10,
    "C":-100
}
class Solution:

    # TODO: Refactor until pretty.
    def romanToInt(self, s: str) -> int:
        the_int =0
        skip_next = False

        for i, char in enumerate(s):
            # if skip_next:
            #     skip_next = False
            #     continue
            if (i+1)<len(s):
                upcoming = s[i+1]
            else:
                upcoming = ""
            if char == "I" and upcoming in ("V", "X"):
                nully_number = -1
                skip_next = True
                the_int += nully_number
            elif char == "X" and upcoming in ("L", "C"):
                nully_number = -10
                skip_next = True
                the_int += nully_number
            elif char == "C" and upcoming in ("D", "M"):
                nully_number = -100
                skip_next = True
                the_int += nully_number
            else:
                nully_number = romans.get(char)
                if char:
                    number = nully_number
                    the_int += number
                else:
                    raise TypeError("Bad input")
        return the_int