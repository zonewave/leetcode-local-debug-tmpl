
code filename

```sh
test_$!{question.frontendQuestionId}_$!velocityTool.snakeCaseName(${question.titleSlug})
```

code template content

```cpp
${question.content}
\#include "common.h"

namespace L9
{
   ${question.code}

    TEST_CASE("test cases")
    {
        vector<LTestCase<
                ?, // want type: for example:  "ListNode*" , , note: must add ","
                ? // args type : for example:  "ListNode*,ListNode*"
            >>
            cases = {
                {
                    "case 1",
                    ?, // want
                    ?, // args
                },
                // add cases
            };
        for (const auto& case_ : cases)
        {
            SUBCASE(case_.name.c_str())
            {
                Solution s;
                auto arg1 = case_.args.get<0>();
                // auto arg2 = case_.args.get<1>();
                // 1. may be replace function name,2, may be add/sub args
                auto result = s.$!velocityTool.snakeCaseName(${question.titleSlug})(arg1);
                // note: use ListNode::eq when compare ListNode
                CHECK(result == case_.want);
            }
        }
    }
}


```