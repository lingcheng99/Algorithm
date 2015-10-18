"""
LeetCode question: reverse a singly linked list
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution:
    def reverseList(self,head):
        if head==None:
            return
        reverse=None
        while head!=None:
            current=head
            head=head.next
            current.next=reverse
            reverse=current
        return reverse
