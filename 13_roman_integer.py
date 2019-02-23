#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-23 11:19
# @Author  : ZD Liu

class Solution():
    def romanToInt(self, x: 'str'):
        dic_value = {}
        dic_value['I'] = 1
        dic_value['V'] = 5
        dic_value['X'] = 10
        dic_value['L'] = 50
        dic_value['C'] = 100
        dic_value['D'] = 500
        dic_value['M'] = 1000
        value = 0
        for i in range(len(x)-1):
            if dic_value[x[i]] >= dic_value[x[i+1]]:
                value = dic_value[x[i]] + value
            else:
                value = value - dic_value[x[i]]
        # print(value+dic_value[x[-1]])
        return value+dic_value[x[-1]]


    def romanToInt2(self, s: 'str'):
        value, prevValue, result = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}, None, 0
        for ch in s:
            currValue = value[ch]
            result += currValue
            if prevValue and currValue > prevValue:
                result -= 2 * prevValue
            prevValue = currValue
        # print(result)
        return result

if __name__ == '__main__':
    solution = Solution()
    s = "MCMXCIV"
    solution.romanToInt2(s)