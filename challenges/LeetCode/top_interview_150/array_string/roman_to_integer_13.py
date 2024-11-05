"""
The problem requires converting a Roman numeral to an integer by following specific rules:
- Each symbol has a value, but if a smaller numeral is placed before a larger one, 
  we subtract it instead of adding it.
  
My initial thought is to iterate through the string, comparing each character with the 
next one. If a character is smaller than the one that follows, I’ll subtract its value;
otherwise, I’ll add it.
"""

class Solution(object):
    def romanToInt(self, s):
        """All inputs provided by LeetCode"""
        ans = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Iterate through pairs of adjacent characters
        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                ans -= roman[a]  # Subtract if the previous is less than the next
            else:
                ans += roman[a]  # Otherwise, add the value
        
        # Add the value of the last character, as it has no adjacent pair to compare
        return ans + roman[s[-1]]
