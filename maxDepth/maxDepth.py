'''
Author: Ezreal
Date: 2020-10-21 21:01:09
LastEditTime: 2020-10-21 21:12:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /algorithm/maxDepth/maxDepth.py
'''
"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        hl = self.maxDepth(root.left)
        hr = self.maxDepth(root.right)
        return max(hl,hr)+1