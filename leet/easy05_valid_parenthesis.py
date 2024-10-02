# stuck. This ID's some but doesn't handle nested e.g. "([)]"
# probably needs some state machine or something
# to track when "inside an unclosed block"

class Solution:
    def isValid(self, s: str) -> bool:
        round = 0
        curly = 0
        square = 0
        nested = False
        for char in s:
            if char == "(":
                round += 1
            elif char == ")":
                round -= 1
            elif char == "{":
                curly += 1
            elif char == "}":
                curly -= 1
            elif char == "[":
                square += 1
            elif char == "]":
                square -= 1
            # if round !=0 and char in ("]", "}"):
            #     return False
            # if square !=0 and char in (")", "}"):
            #     return False
            # if curly !=0 and char in ("]", ")"):
            #     return False
        return curly == 0 and square == 0 and round == 0



