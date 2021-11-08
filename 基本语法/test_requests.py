import requests
'''
r = requests.get('https://www.baidu.com')
#打印返回状态码
print(r.status_code)
#打印编码
print(r.encoding)
#返回结果有乱码，那就指定编码格式为utf-8
r.encoding= "utf-8"
#查看返回结果
print(r.text)
'''
r = requests.post("http://httpbin.org/post", data={'key':'value'})
print(r.status_code)
print(r.encoding)
print(r.text)