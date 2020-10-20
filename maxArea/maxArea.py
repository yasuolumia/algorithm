# coding=utf-8
'''
Author: Ezreal
Date: 2020-10-20 14:42:10
LastEditTime: 2020-10-20 16:10:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /algorithm/maxArea/maxArea.py
'''
"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。


图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

s = 底*高 横坐标为9-2，纵坐标为7 所以s = 7*7=49
换算成索引就是8-1 = 7

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            buttom = abs(j - i)
            high = min(height[i], height[j])
            s = buttom * high
            maxArea = max(s, maxArea)
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return maxArea


if __name__ == "__main__":
    a = Solution()
    s = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    a.maxArea(s)
