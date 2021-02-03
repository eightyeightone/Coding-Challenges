#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wednesday 20 January 2021.
Finished on
@author: h.
References:
https://projecteuler.net/about
"""
#------------------------------------------------------------------------------#
""" Question.
Alex works at a clothing store. There is a large pile of socks that must be
paired by color for sale. Given an array of integers representing the color of
each sock, determine how many pairs of socks with matching colors there are.

For example, there are n = 7 socks with colors ar = [1,2,1,2,1,3,2]. There is
one pair of color 1 and one of color 2. There are three odd socks left, one of
each color. The number of pairs is 2.

Function Description:

Complete the sockMerchant function in the editor below. It must return an
integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

Input Format:
The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors
    ar[i] of the socks in the pile.

Constraints:
    1 <= n <= 100
    1 <= ar[i] <= 100, where 0 <= i < n

Output Format:
Return the total number of matching paris of socks that alex can sell.
"""
#------------------------------------------------------------------------------#
import math
import os
import random
import re
import sys

from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs_socks = 0
    for val in Counter(ar).values():
        pairs_socks += (val//2)

    return pairs_socks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
