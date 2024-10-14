code filename

```sh
test_$!{question.frontendQuestionId}_$!velocityTool.snakeCaseName(${question.titleSlug})
```

code template content

```python
${question.content}
from precompiled.all import *
${question.code}


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