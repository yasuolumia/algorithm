'''
Author: Ezreal
Date: 2020-10-20 22:08:59
LastEditTime: 2020-10-20 22:29:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /algorithm/preorderTraversal/preorderTraversal.py
'''
"""
144. 二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        top = -1
        res = []
        s = []
        while root is not None or top != -1:
            while root is not None:
                res.append(root.val)
                top += 1
                s.append(root)
                root = root.left
            if top != -1:
                top -= 1
                root = s.pop()
                root = root.right
        return res