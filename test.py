import requests
import json

'''面向过程编程'''
# '''实例一  一个get接口: http://39.98.138.157:5001/api/demo'''
#
# # 接口地址
# url='http://39.98.138.157:5001/api/demo'
#
# # 参数，其类型为json格式
# data={"limit":"1"}  # 字典类型
# data=json.dumps(data)# 将字典转换成json字符串
#
# # 请求头
# headers={"Content-Type":"application/json"}# 字典类型
#
# # res：接受请求得到的响应值
# res=requests.get(url=url,params=data,headers=headers)# 发送请求，返回接口消息体
# print('第一个接口',res.text,res.status_code)# 打印res的文本、状态
#
#
# '''实例二  一个post接口: http://39.98.138.157:5001/api/login'''
# # 接口地址
# url='http://39.98.138.157:5001/api/login'
#
# # 参数，其类型为json格式
# data={"username":"admin","password":"123456"}  # 字典类型
# data=json.dumps(data)# 将字典转换成json字符串
#
# # 请求头
# headers={"Content-Type":"application/json"}# 字典类型
#
# # res：接受请求得到的响应值
# res=requests.post(url=url,data=data,headers=headers)# 发送请求，返回接口消息体
# print("第二个接口",res.text,res.status_code)# 打印res的文本、状态


'''封装：面向函数编程'''
# def test_demo():
#     # 接口地址
#     url = 'http://39.98.138.157:5001/api/demo'
#
#     # 参数，其类型为json格式
#     data = {"limit": "1"}  # 字典类型
#     data = json.dumps(data)  # 将字典转换成json字符串
#
#     # 请求头
#     headers = {"Content-Type": "application/json"}  # 字典类型
#
#     # res：接受请求得到的响应值
#     res = requests.get(url=url, params=data, headers=headers)  # 发送请求，返回接口消息体
#     print('第一个接口', res.text, res.status_code)  # 打印res的文本、状态
#
# def test_login():
#     # 接口地址
#     url = 'http://39.98.138.157:5001/api/login'
#
#     # 参数，其类型为json格式
#     data = {"username": "admin", "password": "123456"}  # 字典类型
#     data = json.dumps(data)  # 将字典转换成json字符串
#
#     # 请求头
#     headers = {"Content-Type": "application/json"}  # 字典类型
#
#     # res：接受请求得到的响应值
#     res = requests.post(url=url, data=data, headers=headers)  # 发送请求，返回接口消息体
#     print("第二个接口", res.text, res.status_code)  # 打印res的文本、状态

# test_demo()
# test_login()


'''
    unitest，HtmlTestRuner用例组织框架，测试报告，pytest：这里讲的是最简单的一个命令
    unitest+pytest可相结合使用
'''
# 读写yaml文件
import yaml
def read_yaml():
    with open(r"C:\Users\Administrator\Desktop\软件测试\Learn_Interface_Test\config\data.yaml", 'r')as f: # 前面加个r是防止转页
        cfg = yaml.load(f.read())
        return cfg

data = read_yaml()
print(data['api_url'])
url = data['api_url']


from logger import logger
# 用例
import unittest
class TestCase(unittest.TestCase):
    ''' 这里最好只写测试用例请求 '''

    def test_demo(self):
        # 接口地址
        # url = 'http://39.98.138.157:5001/api/demo'

        # 参数，其类型为json格式
        data = {"limit": "1"}  # 字典类型
        data = json.dumps(data)  # 将字典转换成json字符串

        # 请求头
        headers = {"Content-Type": "application/json"}  # 字典类型

        # res：接受请求得到的响应值
        res = requests.get(url=url + 'demo', params=data, headers=headers)  # 发送请求，返回接口消息体
        # print('第一个接口', res.text, res.status_code)  # 打印res的文本、状态
        # logger.info(res.json())
        logger.info(res.text)

    def test_login(self):
        # 接口地址
        # url = 'http://39.98.138.157:5001/api/login'

        # 参数，其类型为json格式
        data = {"username": "admin", "password": "123456"}  # 字典类型
        data = json.dumps(data)  # 把python类型转化为json字符串（将字典转换成字符串）

        # 请求头
        headers = {"Content-Type": "application/json"}  # 字典类型

        # res：接受请求得到的响应值
        res = requests.post(url=url + 'login', data=data, headers=headers)  # 发送请求，返回接口消息体
        # print("第二个接口", res.text, res.status_code)  # 打印res的文本、状态
        # logger.info(res.json())
        logger.info(res.text)


if __name__ == '__main__':
    unittest.main()
    # import pytest
    # pytest.main(['-s','test.py','--html=yideng.html'])
