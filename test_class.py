# Used to group related tests together

## TestClass cannot have an `__init__`
## Each test method gets a unique instance of test class


class TestClass:

    @staticmethod
    def test_one():
        assert 5 == 5

    def test_two(self):
        assert 10 == 10
