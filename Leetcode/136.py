# from https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = nums_dict.setdefault(i, 1)
            else:
                nums_dict[i] = nums_dict.get(i, 0) + 1
        res = [k for k, v in nums_dict.items() if v == 1]
        return res[0]
    
case1 = [2, 2, 1]
case2 = [4, 1, 2, 1, 2]
case3 = [1]

print(Solution().singleNumber(case1))
print(Solution().singleNumber(case2))
print(Solution().singleNumber(case3))
