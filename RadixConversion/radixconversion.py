# coding=utf-8
'''
Author: your name
Date: 2021-01-20 17:22:33
LastEditTime: 2021-01-20 18:00:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /algorithm/RadixConversion/radixconversion.py
'''
"""
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
输入：
0xA
0xAA
输出：
10
170
"""
import sys
radix = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}

def conversion(hexnum):
    sum = 0
    if hexnum.__contains__('0x'):
        elem = hexnum.lower().split('0x')[1]
        for i in xrange(len(elem)):
            sum += radix.get(elem[i])*16**i
        print sum
    else:
        pass


if __name__ == "__main__":
    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == '':
                break
            lines = line.split()
            for i in lines:
                conversion(i)
    except:
        pass