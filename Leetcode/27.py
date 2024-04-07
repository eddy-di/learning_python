# from https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == val:
                    nums[i], nums[j] = nums[j], nums[i]
        slice_index = None
        for i in range(len(nums)):
            if nums[i] == val:
                slice_index = i
                break
        nums = nums[0:slice_index]
        return len(nums)                

    

print(Solution().removeElement([3,2,2,3], 3))
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))