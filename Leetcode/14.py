# from https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans=""
        v=sorted(strs)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans

case1 = ["flower","flow","flight"]
case2 = ["dog","racecar","car"]
case3 = ['car', 'cir']
case4 = ['aa', 'aa']

print(Solution().longestCommonPrefix(case1))
print(Solution().longestCommonPrefix(case2))
print(Solution().longestCommonPrefix(case3))
print(Solution().longestCommonPrefix(case4))