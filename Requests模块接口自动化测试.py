import requests

#get请求指定的页面信息，并返回状态吗
base_url = 'https://httpbin.org'
r = requests.get(base_url + '/get')
print(r.status_code)

#post:向指定资源提交数据
r = requests.post(base_url + '/post')
print(r.status_code)

#delete请求服务器删除指定的页面
r = requests.delete(base_url + '/delete')
print(r.status_code)

#通过get方式传参，打印地址，打印状态码
param_data = {'user':'zhang', 'password':'9999'}
r = requests.get(base_url + '/get', params = param_data)
print(r.url)
print(r.status_code)

#post方式发送数据例子
form_data={'user':'li', 'password':'8888'}
r = requests.post(base_url + '/post', data = form_data)
print(r.url)
print(r.status_code)
print(r.text)
