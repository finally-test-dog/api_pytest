# *coding:utf-8 *
import pytest



class TestThree:

    def setup_method(self):
        print("准备测试数据")

    def teardown_method(self):
        print("清理测试数据")

    def test_one(self):
        num1 = 1
        num2 = 1
        assert num1 == num2

    def test_two(self):
        num1 = 1
        num2 = 2
        assert num1 != num2

if __name__ == '__main__':
    pytest.main(['q', 'test_class.py'])