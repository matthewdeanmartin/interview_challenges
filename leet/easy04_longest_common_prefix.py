from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        # candidate = None
        # j = 1
        # max_possible = max(map(len, strs))

        # all_same = True
        # for lengths in range(1, max_possible):
        #     for word in strs:
        #         # id 1st candidate
        #         if candidate is None:
        #             candidate = word[0:j]
        #         else:
        #             all_same = candidate == word[0:j]
        #             print(all_same, candidate, word[0:j], j)
        #             if not all_same:
        #                 return candidate[0:j-1]
        #     j += 1
        #     candidate = word[0:j]

        longest = ""
        for word in strs:
            if len(word)>len(longest):
                longest= word
        # print("longest", longest)
        candidate = ""
        for i in range(0, len(longest)+1):
            # print(list(word for word in strs if word.startswith(longest[0:i])))
            is_candidate = all(word.startswith(longest[0:i]) for word in strs)
            if is_candidate:
                candidate = longest[0:i]
        return candidate
