# *coding:utf-8 *
import pytest



@pytest.mark.skip
def test_one():
    print("测试")
    num1 = 1
    num2 = 2
    assert num1 == num2

@pytest.mark.skipif('2==2')
def test_two():
    num1 = 1
    num2 = 2
    assert num1 != num2

if __name__ == '__main__':
    pytest.main()