#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-21 22:20
# @Author  : ZD Liu

class Solution:
    def reverseInteger(self, x: 'int'):
        bit_list = []
        q = 1
        if x < 0:
            q = -1
            x = q * x
        while x > 0:
            n = x % 10
            x = x // 10
            bit_list.append(n)
        out_num = 0
        for i in bit_list:
            out_num = out_num * 10 + i
        print(q * out_num)
        return  q * out_num

if __name__ == '__main__':
    solution = Solution()
    x = 120
    solution.reverseInteger(x)

        
