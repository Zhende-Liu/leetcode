#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-23 10:31
# @Author  : ZD Liu


class Solution:
    def isPalindrome(self, x:'int'):
        str_x = str(x)
        len_str = len(str_x)
        for i in range(len_str):
            if str_x[i] == str_x[-(i+1)]:
                pass
            else:
                # print(False)
                return False
        # print(True)
        return True

    def isPalindrome2(self, x: 'int'):
        str_x = str(x)
        len_str = int(len(str_x)/2) + 1
        for i in range(len_str):
            if str_x[i] == str_x[-(i + 1)]:
                pass
            else:
                # print(False)
                return False
        # print(True)
        return True

if __name__ == "__main__":
    solution = Solution()
    num = 1123211
    solution.isPalindrome(num)



