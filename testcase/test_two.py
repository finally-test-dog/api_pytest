# *coding:utf-8 *
import pytest

@pytest.mark.test
def test_one():
    print("测试")
    num1 = 1
    num2 = 2
    assert num1 == num2

@pytest.mark.p0
def test_two():
    num1 = 1
    num2 = 2
    assert num1 != num2