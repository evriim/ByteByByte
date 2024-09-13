"""
The problem requires removing all instances of a specified value from an array, 
modifying the array in place. Initially, my first thought is to iterate through
the array, count the occurrences of the target value, and then remove it.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """All inputs provided by LeetCode"""
        counter=0
        for i in nums:
            if i == val:
                counter+=1
        for i in range(counter):
            nums.remove(val)
        return
