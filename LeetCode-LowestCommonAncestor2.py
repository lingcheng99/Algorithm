"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Notice it is binary tree, not BST
"""

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        elif root.val==p.val or root.val==q.val:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if not left and not right:
                return root
            else:
                if not left:
                    return left
                if not right:
                    return right


