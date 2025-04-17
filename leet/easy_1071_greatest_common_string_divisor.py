# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# This solution was accepted.

class Solution:
    def divides(self, str1:str, str2:str)->bool:
        product = ""
        longest =max(len(str1),len(str2))
        longer = str1 if len(str1)>len(str2) else str2
        shorter = str1 if len(str1)>len(str2) else str2
                
        count = 0
        while len(product) < len(longer):
            product = shorter * count
            if longer == product:
                return True
            count += 1 
            if count>50:
                break
        return False

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longer = str1 if len(str1)>len(str2) else str2
        shorter = str1 if len(str1)>len(str2) else str2

        candidates = []
        for i in range(0,len(longer)):
            part = str1[0:i]
            if self.divides(str2, part):
                candidates.append(part)
        if not candidates:
            return ""
        return list(sorted(candidates, key=len))[0]
        
