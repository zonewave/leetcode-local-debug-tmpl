/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

#include "common.h"

class Solution
{
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode *head = nullptr, *tail = nullptr;
        int carry = 0;
        while (l1 || l2)
        {
            int n1 = l1 ? l1->val : 0;
            int n2 = l2 ? l2->val : 0;
            int sum = n1 + n2 + carry;
            if (!head)
            {
                head = tail = new ListNode(sum % 10);
            }
            else
            {
                tail->next = new ListNode(sum % 10);
                tail = tail->next;
            }
            carry = sum / 10;
            if (l1)
            {
                l1 = l1->next;
            }
            if (l2)
            {
                l2 = l2->next;
            }
        }
        if (carry > 0)
        {
            tail->next = new ListNode(carry);
        }
        return head;
    }
};

// @lc code=end

struct Args
{
    mutable ListNode* l1;
    mutable ListNode* l2;
};

struct LTestCase
{
    std::string name;
    Args args;
    ListNode* want;
};

TEST_CASE("test addTwoNumbers")
{
    Solution s;

    vector<LTestCase> cases = {
        {
            "Test case 1",
            {ListNode::arrayToListNode({1, 2, 3}), ListNode::arrayToListNode({1, 2, 3})},
            ListNode::arrayToListNode({2, 4, 6}),
        }
        // todo add tests
    };

    for (const auto& case_ : cases)
    {
        SUBCASE(case_.name.c_str())
        {
            auto result = s.addTwoNumbers(case_.args.l1, case_.args.l2);
            CHECK(result->eq(result,case_.want));
    
        }
    }
}

