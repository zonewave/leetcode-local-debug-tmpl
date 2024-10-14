# Given an array of integers nums and an integer target, return indices of the 
# two numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may 
# not use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  Only one valid answer exists. 
#  
# 
#  
# Follow-up: Can you come up with an algorithm that is less than 
# O(n²)
#  time complexity?
# 
#  Related Topics Array Hash Table 👍 58036 👎 2055

from precompiled.all import  *
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
@dataclass
class Args:
  nums: list[int]  # replace
  target: int  # replace

@dataclass
class LTestCase:
  name: str
  args: Args
  want: list[int]  #replace

class TestSolution(TestCase):
  def test_two_sum(self):
    cases: list[LTestCase] = [
      # add arg
      LTestCase("1", Args([2, 7, 11, 15], 9), [0, 1]),
      LTestCase("2", Args([3, 2, 4], 6), [1, 2]),
      LTestCase("3", Args([3, 3], 6), [0, 1])
    ]
    s = Solution()
    for case in cases:
      with self.subTest(case=case.name):
        # may be replace func name
        self.assertEqual(s.twoSum(**case.args.__dict__), case.want)
