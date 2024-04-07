# from https://leetcode.com/problems/set-mismatch/?envType=daily-question&envId=2024-01-22


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        size = len(nums)
        expected = [i for i in range(1, size + 1)]
        missing = set(expected).difference(set(nums))
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = nums_dict.setdefault(i, 1)
            else:
                nums_dict[i] = nums_dict.get(i, 0) + 1
        duplicate = [k for k, v in nums_dict.items() if v == 2]
        res = duplicate + list(missing)
        return res
    
case1 = [1,2,2,4]
case2 = [1,1]

print(Solution().findErrorNums(case1))
print(Solution().findErrorNums(case2))