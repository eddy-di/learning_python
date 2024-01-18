# from https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = nums_dict.setdefault(i, 1)
            else:
                nums_dict[i] = nums_dict.get(i, 0) + 1
        unique = [k for k in nums_dict.keys()]
        for i in range(len(unique)):
            if nums[i] != unique[i]:
                for j in range(i+1, len(nums)):
                    if nums[j] == unique[i]:
                        nums[j], nums[i] = nums[i], nums[j]
        return len(unique)
    

a = Solution()
a.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
