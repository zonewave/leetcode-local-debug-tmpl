import json

py = """
from precompiled.all import *

class TestSolution(TestCase):
    # replace name
    def test_$1(self):
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
                self.assertEqual(s.$1(case.args.get(0),case.args.get(1)), case.want)
"""
cppHead = """
#include "common.h"
namespace L?{
"""
cppBody = """
    TEST_CASE("test cases"){
        vector<LTestCase<
            ?,//want
            ? //args
            >>
            cases ={
            {
                "case 1",
               ?, //want
               ?, //args
            },
            // add cases
        };
        for (const auto& case_ : cases)
        {
            SUBCASE(case_.name.c_str())
            {
                Solution s;
                auto arg1 = case_.args.get<0>();
                auto arg2 = case_.args.get<1>();
                // replace args 
                vector<int> result = s.?(arg1, arg2);
                // note: use ListNode::eq when compare ListNode
                CHECK(result == case_.want);
            }
        }
    }
}
"""


def print_json(tmpl):
    code_lines = tmpl.split("\n")
    code_json = json.dumps(code_lines)
    print(code_json)


if __name__ == '__main__':
    print_json(py)
    # print_json(cppBody)
