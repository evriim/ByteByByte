"""
The problem involves merging two sorted arrays, nums1 and nums2,
where nums1 has enough space at the end to accommodate nums2. 
Since both arrays are sorted, the idea is to fill nums1 starting
from the end, which avoids overwriting elements in nums1 while still
merging efficiently.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """All inputs provided by LeetCode"""
        rep =0
        for i in range(m,len(nums1)):
            if nums1[i] ==0:
                nums1[i] = nums2[rep]
                rep +=1
        return nums1.sort()
