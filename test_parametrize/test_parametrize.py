# *coding:utf-8 *
import pytest

# @pytest.mark.parametrize('a',['b','c'])
# def test_paramertrize_01(a):
#     print(a)
#     print("测试结束")

# 数组
# @pytest.mark.parametrize('name,age',[['景甜', 24],['热巴', 25]])
#元组
# @pytest.mark.parametrize('name,age',[('景甜', 24),('热巴', 25)])
# def test_paramertrize_01(name,age):
#     print(name,age)
#     assert name == '景甜'

# 字典
@pytest.mark.parametrize('data',[{'name':'景甜', 'age':24},{'name':'热巴', 'age':25}])
def test_paramertrize_01(data):
    print(data['name'],data['age'])
    assert data['name'] == '景甜'