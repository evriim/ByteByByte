"""
The problem requires merging two sorted arrays (`nums1` and `nums2`) into `nums1` in a sorted order.
`nums1` has enough space to hold the elements of both arrays, with its initial elements up to index `m-1`
being the valid elements, and the rest (from index `m` onward) being zeros.

My approach is to place elements from `nums2` into the empty slots of `nums1` (after `m`) and then sort `nums1`.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """All inputs provided by LeetCode"""
        rep = 0  # Initialize a pointer for nums2
        
        # Replace zeros in nums1 from index m to the end with elements from nums2
        for i in range(m, len(nums1)):
            if nums1[i] == 0:
                nums1[i] = nums2[rep]
                rep += 1
        
        # Sort nums1 to combine the elements in sorted order
        return nums1.sort()
