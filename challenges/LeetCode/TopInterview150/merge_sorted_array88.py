"""
nums1 has a size of m + n, where the first m elements are valid and the last n elements are placeholders (zeros) for the elements from nums2.
nums2 has n valid elements.
The goal is to merge both arrays in non-decreasing order directly into nums1.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        rep =0
        for i in range(m,len(nums1)):
            if nums1[i] ==0:
                nums1[i] = nums2[rep]
                rep +=1        
        return nums1.sort()
