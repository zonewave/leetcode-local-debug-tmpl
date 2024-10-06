code filename

```sh
test_$!{question.frontendQuestionId}_$!velocityTool.snakeCaseName(${question.titleSlug})
```

code template content

```python
${question.content}
from precompiled.all import *
${question.code}


@dataclass
class Args:
    arg1: T1  # replace
    arg2: T2  # replace


@dataclass
class LTestCase:
    name: str
    args: Args
    want: T3  # replace


class TestSolution(TestCase):
    def test_$!velocityTool.snakeCaseName(${question.titleSlug})(self):
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
                self.assertEqual(s.$!velocityTool.smallCamelCaseName(${question.titleSlug})(**case.args.__dict__), case.want)

```