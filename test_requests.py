import requests

r = requests.get("http://www.baidu.com")
"""
获取一个get请求
"""
print(r.text)
"""
打印返回值
"""

r = requests.post('http://httpbin.org/post', data={'key':'value'})
"""
获取一个post请求
"""
print(r.text)
"""
打印获取到的post返回值
"""
r.status_code
"""
访问请求返回的状态码 200为成功，404 500等表示请求失败
"""
r.encoding
"""
查看编码
"""
r.encoding="utf-8"
"""
设置编码格式
"""