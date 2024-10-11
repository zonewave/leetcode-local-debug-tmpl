
code filename

```sh
test_$!{question.frontendQuestionId}_$!velocityTool.snakeCaseName(${question.titleSlug})
```

code template content

```python
${question.content}
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

from precompiled.listnode import ListNode
from precompiled.nestedinteger import NestedInteger
from precompiled.treenode import TreeNode
from precompiled.node import Node
from precompiled.testcase import LTestCase

from typing import *
from unittest import TestCase
from dataclasses import dataclass



class TestSolution(TestCase):
    def test_$!velocityTool.snakeCaseName(${question.titleSlug})(self):
        cases: list[LTestCase] = [
            # add result and args
            LTestCase("1", want, *args),
            # LTestCase("2", want, *args),
            # LTestCase("3", want, *args),
        ]
        s = Solution()
        for case in cases:
            with self.subTest(case=case.name):
                # may be replace func name
                self.assertEqual(s.$!velocityTool.smallCamelCaseName(${question.titleSlug})(case.args.get(0),case.args.get(1)), case.want)

```