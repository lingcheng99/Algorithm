"""
Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"]. 
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        alist=[]
        i=0
        while i<len(nums)-1:
            while nums[i]!=nums[i+1]-1:
                i+=1
            if i<len(nums):
                head=nums[i]
        
            while i<len(nums)-1 and nums[i]==nums[i+1]-1:
                i+=1
            if head<nums[i]:
                tail=nums[i]
                alist.append(str(head)+'->'+str(tail))
            i+=1
        return alist
