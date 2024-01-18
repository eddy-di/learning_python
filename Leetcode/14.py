# from https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        length = len(strs)
        common_prefixes = {}
        for i in strs:
            word_dict = {}
            for c in i:
                if c not in word_dict:
                    word_dict[c] = word_dict.get(c, 0) + 1
                else:
                    word_dict[c] = word_dict.get(c, 0) + 1
            for k, v in word_dict.items():
                if v > 1:
                    v = 1
                    common_prefixes[k] = common_prefixes.get(k, 0) + 1
                else:
                    common_prefixes[k] = common_prefixes.get(k, 0) + 1
                    
        for k, v in common_prefixes.items():
            if v == length:
                res += k

        return res

case1 = ["flower","flow","flight"]
case2 = ["dog","racecar","car"]

print(Solution().longestCommonPrefix(case1))
print(Solution().longestCommonPrefix(case2))