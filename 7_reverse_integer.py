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

        if out_num >= 2**31 or out_num <= -2**31:
            print(0)
            return 0
        print(q * out_num)
        return  q * out_num
    def reverseInteger2(self, x: 'int'):
        q = 1
        if x < 0:
            q = -1
            x = q * x
        out_num = 0
        while x > 0:
            n = x % 10
            x = x // 10
            out_num = out_num * 10 + n
        if out_num >= 2**31 or out_num <= -2**31:
            print(0)
            return 0
        print(out_num)
        return  q*out_num

    def reverseInteger3(self, x):
        a = str(x)[::-1] # let str(x) output all letters from the last one
        if x < 0:
            res = int('-{0}'.format(a[:-1]))
        else:
            res = int(a)
        if res <= 2 ** 31 - 1 and res >= -2 ** 31:
            return res
        print(res)
        return 0

if __name__ == '__main__':
    solution = Solution()
    x = -34236469
    solution.reverseInteger3(x)

        
