# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  只会存在一个有效答案 
#  
# 
#  
# 
#  进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？ 
# 
#  Related Topics 数组 哈希表 👍 18877 👎 0
from precompiled.all import *

from typing import *
from unittest import TestCase
from dataclasses import dataclass
@dataclass
class Args:
  nums: list[int]
  target: int


@dataclass
class LTestCase:
  name: str
  args: Args
  want: list[int]


class TestSolution(TestCase):
  def test_two_sum(self):

    cases: list[LTestCase] = [
      LTestCase("1", Args([2, 7, 11, 15], 9), [0, 1]),
      LTestCase("2", Args([3, 2, 4], 6), [1,2]),
      LTestCase("3", Args([3, 3], 6), [0, 1])
    ]
    s = Solution()
    for case in cases:
      with self.subTest(case=case.name):
        self.assertEqual(s.twoSum(**case.args.__dict__), case.want)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index_map = {}
    for index, num in enumerate(nums):
      prior = index_map.get(target - num)
      if prior is not None:
        return [prior, index]
      index_map[num] = index

    return None

# leetcode submit region end(Prohibit modification and deletion)
