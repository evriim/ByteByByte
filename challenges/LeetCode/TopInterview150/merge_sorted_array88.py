"""
This problem is about merging two sorted integer arrays, nums1 and nums2, into one sorted array. 
The array nums1 has additional space at the end to accommodate the elements from nums2,
and the task is to modify nums1 in-place.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        rep =0
        for i in range(m,len(nums1)):
            if nums1[i] ==0:
                nums1[i] = nums2[rep]
                rep +=1        
        return nums1.sort()
