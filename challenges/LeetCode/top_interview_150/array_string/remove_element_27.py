"""
The problem requires removing all instances of a specified value (`val`) from an array (`nums`), 
modifying the array in place. 

My initial thought is to iterate through the array to count how many times `val` appears. 
Once I know the count, I can remove `val` from `nums` that many times.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """All inputs provided by LeetCode"""
        counter = 0  # Initialize a counter to count occurrences of `val`
        
        # First loop: Count how many times `val` appears in `nums`
        for i in nums:
            if i == val:
                counter += 1  # Increment the counter each time `val` is found
        
        # Second loop: Remove `val` from `nums` exactly `counter` times
        for i in range(counter):
            nums.remove(val)
        
        # Function does not need to return anything as `nums` is modified in place
        return

