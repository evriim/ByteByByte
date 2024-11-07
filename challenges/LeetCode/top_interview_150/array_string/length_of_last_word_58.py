"""
The problem requires finding the length of the last word in a given string `s`.
A word is defined as a maximal substring consisting of non-space characters only.

My approach is to split the string into a list of words, then return the length of the last word in that list.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        # Split the string `s` into a list of words by whitespace
        word = s.split()
        
        # Get the length of the last word in the list
        a = len(str(word[-1]))
        
        # Return the length of the last word
        return a
