# *coding:utf-8 *
import pytest

@pytest.mark.pro

class TestThree:

    def test_one(self):
        num1 = 1
        num2 = 2
        assert num1 == num2

    def test_two(self):
        num1 = 1
        num2 = 2
        assert num1 != num2