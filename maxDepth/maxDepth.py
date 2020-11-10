# coding=utf-8
'''
Author: Ezreal
Date: 2020-10-21 21:01:09
LastEditTime: 2020-11-06 11:14:50
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
class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        hl = self.maxDepth(root.lchild)
        hr = self.maxDepth(root.rchild)
        return max(hl, hr) + 1


class BinaryTree:
    """二叉树"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """广度优先遍历方式添加节点"""
        if self.root is None:
            self.root = Node(item)
        else:
            queue = list()
            queue.append(self.root)

            while len(queue) > 0:
                node = queue.pop(0)
                if not node.lchild:
                    node.lchild = Node(item)
                    return
                else:
                    queue.append(node.lchild)
                if not node.rchild:
                    node.rchild = Node(item)
                    return
                else:
                    queue.append(node.rchild)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = list()
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.item)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    def preorder_travel(self, root):
        """先序 根 左 右"""
        if root:
            print(root.item)
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)

    def inorder_travel(self, root):
        """中序 左 根 右"""
        if root:
            self.inorder_travel(root.lchild)
            print(root.item)
            self.inorder_travel(root.rchild)

    def postorder_travel(self, root):
        """后序 左 右 根"""
        if root:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        hl = self.maxDepth(root.lchild)
        hr = self.maxDepth(root.rchild)
        return max(hl, hr) + 1


if __name__ == "__main__":
    tree = BinaryTree()
    data = [3, 9, 20, None, None, 15, 7]
    for item in data:
        tree.add(item)
    tree.breadth_travel()
    print("")
    tree.preorder_travel(tree.root)
    print("")
    tree.inorder_travel(tree.root)
    print("")
    tree.postorder_travel(tree.root)
    print("")
    a = tree.maxDepth(tree.root)
    print a
