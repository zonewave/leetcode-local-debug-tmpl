#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] Add Two Numbers
#


from precompiled.all import *

class TestSolution(TestCase):
    # replace name
    def test_addTwoNumbers(self):
        cases: list[LTestCase] = [
             # add result and args
            LTestCase("1", ListNode.array_to_list_node([7,0,8]),  ListNode.array_to_list_node([2,4,3]), ListNode.array_to_list_node([5,6,4])),
            # LTestCase("2", want, *args),
            # LTestCase("3", want, *args),
        ]
        s = Solution()
        for case in cases:
            with self.subTest(case=case.name):
                # may be replace func name
                self.assertEqual(s.addTwoNumbers(case.args.get(0),case.args.get(1)), case.want)
          
# leetcode submit region begin(Prohibit modification and deletion)      
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry =0
        pre =ListNode(0)
        curr = pre
        while l1  or l2:
            x,y =0,0
            if l1:
                x = l1.val
            if l2:
                y = l2.val
            tot = x + y + carry
            carry = tot//10
            valT = tot % 10
            curr.next = ListNode(valT)
            curr = curr.next
           
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return pre.next
# @lc code=end
# leetcode submit region end(Prohibit modification and deletion)



