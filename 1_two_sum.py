#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-21 21:33
# @Author  : ZD Liu


class Solution:
    def twoSum(self, num_list:'list[int]', target:'int'):
        for i in range(len(num_list)):
            n = i+1
            while numlist[n]:
                if num_list[i] + num_list[n] == target:
                    # print (i, n)
                    res_list = [i, n]
                    return res_list
                n += 1


if __name__ == '__main__':
    solution = Solution()
    numlist = [2, 7, 11, 15]
    target = 9
    print (solution.twoSum(numlist,target))