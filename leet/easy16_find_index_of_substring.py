class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        # Assuming I can't google. Need instr or the like, but for python
        for i in range(0,len(haystack)):
            # print(i, haystack[i:i+len(needle)], needle)
            if haystack[i:i+len(needle)] == needle:
                return i
        # shouldn't get here
        return -1

assert Solution().strStr("hello","ll")==2
assert Solution().strStr("abc","a")==0
assert Solution().strStr("abc","z")==-1