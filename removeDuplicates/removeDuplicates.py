
# coding=utf-8
'''
Author: Ezreal
Date: 2020-10-20 11:36:02
LastEditTime: 2020-10-29 11:54:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /algorithm/removeDuplicates/removeDuplicates.py
# '''
"""
26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)

class RemoveDuplicate(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                if i == 0:
                    nums = [] + nums[i + 1:]
                else:
                    nums = nums[:i] + nums[i + 1:]
            else:
                i += 1
        return len(nums)

# 双指针，修改数组前面n个元素，不用删除
class RemoveDuplicate2(object):
    def removeDuplicates(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i] = nums[j]
                j+=1
        return i+1

if __name__ == "__main__":
    a = Solution()
    b = RemoveDuplicate()
    c = RemoveDuplicate2()
    nums = [1, 1, 2]
    # a.removeDuplicates(nums)
    # print a.removeDuplicates(nums)
    print b.removeDuplicates(nums)
    print c.removeDuplicates(nums)
