"""
The problem requires removing duplicates from a sorted array (`nums`) in-place, ensuring each unique element appears only once.
The result should be the length of the array after duplicates have been removed, with the unique elements at the start of the array.

My initial thought is to use two pointers: 
- `j` to mark the last unique element's position.
- `i` to iterate through the array and find the next unique element.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """All inputs provided by LeetCode"""
        if not nums:
            return 0  # Return 0 if the input array is empty
        
        j = 0  # Initialize `j` to the position of the first element
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:  # Check if current element is unique
                j += 1  # Move `j` to the next position for a unique element
                nums[j] = nums[i]  # Update `nums[j]` to hold the current unique element
        
        # Return the length of the array with unique elements only, which is `j + 1`
        return j + 1
