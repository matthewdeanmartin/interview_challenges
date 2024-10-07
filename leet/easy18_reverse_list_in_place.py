from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(0,len(s)):
            if i>=len(s)/2:
                break
            # print(s[i], s[len(s)-i-1])
            temp =s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1] = temp

assert Solution().reverseString(["h","e","l","l","o"]) ==["o","l","l","e","h"]