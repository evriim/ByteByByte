"""
This problem asks you to remove all occurrences of a specified value (val) from an integer array (nums) in-place,
meaning without using extra space for another array. After removing the occurrences of val,
the task is to return the number of remaining elements (k) that are not equal to val.
"""
class Solution(object):
    def removeElement(self, nums, val):
        counter=0
        for i in nums:
            if i == val:
                counter+=1
        for i in range(counter):
            nums.remove(val)
        return

        
