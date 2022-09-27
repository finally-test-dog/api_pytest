# *coding:utf-8 *
import yaml
import os

# f = open("../config/data.yaml", encoding="utf-8")
# data = yaml.safe_load(f)
# print(data)
path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml")

def read_data():
    f = open(path, encoding="utf-8")
    data = yaml.safe_load(f)
    return data


get_data = read_data()
print(get_data)
