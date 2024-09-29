/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] Two Sum
 */

#include "common.h"
namespace L1
{

    // @lc code=start
    class Solution
    {
    public:
        vector<int> twoSum(vector<int> &nums, int target)
        {
            return {0, 1};
        }
    };
    // @lc code=end

    TEST_CASE("test cases")
    {
        vector<LTestCase<
            vector<int>,     // want
            vector<int>, int // args
            >>
            cases = {
                {
                    "case 1",
                    {0, 1}, // want
                    {2, 3},
                    5, // args
                },
                // add cases
            };
        for (const auto &case_ : cases)
        {
            SUBCASE(case_.name.c_str())
            {
                Solution s;
                auto arg1 = case_.args.get<0>();
                auto arg2 = case_.args.get<1>();
                // replace args
                vector<int> result = s.twoSum(arg1, arg2);
                // note: use ListNode::eq when compare ListNode
                CHECK(result == case_.want);
            }
        }
    }
}
