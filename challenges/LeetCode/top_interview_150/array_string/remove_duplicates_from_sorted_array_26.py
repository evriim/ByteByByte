"""
Since the array is sorted, duplicates will always be next to each other.
This allows us to efficiently remove duplicates by iterating through the
array once and overwriting duplicates in place. By maintaining a pointer
for the next unique element, we can avoid the need for additional memory
and achieve the result in linear time.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """All inputs provided by LeetCode"""
        if not nums:
            return 0
        
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        
        return j + 1
