# *coding:utf-8 *
import pytest

def setup_module():

    print("准备测试数据")

def teardown_module():

    print("清理测试数据")

def test_one():
    print("测试")
    num1 = 1
    num2 = 1
    assert num1 == num2


def test_two():
    num1 = 1
    num2 = 2
    assert num1 != num2

if __name__ == '__main__':
    pytest.main(['q','test_module.py'])