# Given an input string s and a pattern p, implement regular expression 
# matching with support for '.' and '*' where: 
# 
#  
#  '.' Matches any single character. 
#  '*' Matches zero or more of the preceding element. 
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, 
# by repeating 'a' once, it becomes "aa".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 20 
#  1 <= p.length <= 20 
#  s contains only lowercase English letters. 
#  p contains only lowercase English letters, '.', and '*'. 
#  It is guaranteed for each appearance of the character '*', there will be a 
# previous valid character to match. 
#  
# 
#  Related Topics String Dynamic Programming Recursion 👍 12264 👎 2194

from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *

import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json

from unittest import TestCase
from dataclasses import dataclass
from precompiled.listnode import ListNode
from precompiled.nestedinteger import NestedInteger
from precompiled.treenode import TreeNode

from unittest import TestCase
from dataclasses import dataclass

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
# leetcode submit region end(Prohibit modification and deletion)

@dataclass
class Args:
  arg1: T1  # replace
  arg2: T2  # replace

@dataclass
class LTestCase:
  name: str
  args: Args  
  want: T3  #replace


class TestSolution(TestCase):
  def test_regular_expression_matching(self):
    cases: list[LTestCase] = [
      # add args
      LTestCase("1", Args(), ),
      # LTestCase("2", Args(), ),
      # LTestCase("3", Args(), ),
    ]
    s = Solution()
    for case in cases:
      with self.subTest(case=case.name):
        # may be replace func name
        self.assertEqual(s.regularExpressionMatching(**case.args.__dict__), case.want)
