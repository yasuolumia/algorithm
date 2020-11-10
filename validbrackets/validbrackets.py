#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/10 14:40
# @Author : EzrealLiuYe
# @Site : 
# @File : validbrackets.py
# @Software: PyCharm

class Solution(object):
    @staticmethod
    def match(m, n):
        if m == '(' and n == ')':
            return True
        elif m == '[' and n == ']':
            return True
        elif m == '{' and n == '}':
            return True
        else:
            return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False
        elif len(s) % 2 == 0:
            a = []
            b = []
            for i in s:
                if i in '({[':
                    a.append(i)
                else:
                    if len(a) > 0:
                        res = self.match(a.pop(), i)
                        b.append(res)
                    else:
                        return False
            if len(a) > len(b):
                return False
            if len(a) == len(s):
                return False
            if False in b:
                return False
            else:
                return True
        else:
            return False


if __name__ == '__main__':
    s0 = "({}]"
    s = "([)]"
    s1 = "("
    s2 = "(("
    s3 = "()[]{}"
    s4 = "))"
    s5 = "[[[]"
    s6 = "()"
    K = Solution()
    print K.isValid(s0)
