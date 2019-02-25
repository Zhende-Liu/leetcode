#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 19:39
# @Author  : ZD Liu


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) > 0:
            commen_prefix = strs[0]
            for e in strs:
                com_len = len(commen_prefix)
                len_e = len(e)
                if com_len > len_e:
                    com_len = len_e
                if commen_prefix[:com_len] in e[:com_len]:
                    commen_prefix = commen_prefix[:com_len]
                else:
                    for i in range(com_len+1):
                        if i < com_len:
                            if commen_prefix[:com_len-i] in e[:com_len-i]:
                                commen_prefix = commen_prefix[:com_len-i]
                                break
                        else:
                            return ""
            # print('result')
            return commen_prefix

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cpt = ""
        if (not strs):
            return cpt
        minnum = min([len(x) for x in strs])
        same = True
        for i in range(minnum):
            check = [x[i] for x in strs]
            for i in range(len(check)):
                if (check[i] != check[0]):
                    same = False
            if (same):
                cpt += check[0]
        return cpt



if __name__ =='__main__':
    solution = Solution()
    l = ["flower","flow","flight"]
    # l = ["dog","racecar","car"]

    print(solution.longestCommonPrefix2(l))