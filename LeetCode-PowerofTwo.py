"""
Given an integer, write a function to determine if it is a power of two. 
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while num>0 and num%2==0:
          num=num/2
        return num==1
