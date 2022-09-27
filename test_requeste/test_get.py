# *coding:utf-8 *
import requests

def test_mobile():
    r = requests.get('https://api.github.com/events')
    print(r.json())
    print(r.status_code)
    assert r.status_code == 200

