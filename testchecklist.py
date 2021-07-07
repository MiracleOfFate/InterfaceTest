import json
import unittest
import requests
import jsonpath


class MyTestCase(unittest.TestCase):
    def test_checklist1(self):
        # 请求url
        url = "http://39.98.138.157:5000/api/getbloodchecklist?cardnum=10987"
        res = requests.get(url)
        # print(res)      # <Response [200]>
        # print(res.text)
        # print(res.content)

        # 把Json格式字符串解码转换成Python对象
        resjson = json.loads(res.content)  # 将字符串转化为字典
        # print(resjson)

        result = jsonpath.jsonpath(resjson, "$.cardname")
        # print(result)
        # print(result[0])

        self.assertEqual('张一鸣', result[0])

    def test_checklist2(self):
        url = "http://39.98.138.157:5000/api/getliverchecklist?cardnum=10987"
        # 使用requests.get请求
        res = requests.get(url)
        # print(res)      # <Response [200]>
        # print(res.text)
        # print(res.content)

        # 把Json格式字符串解码转换成Python对象
        resjson = json.loads(res.content)  # 将字符串转化为字典
        # print(resjson)

        result = jsonpath.jsonpath(resjson, "$.cardnum")
        self.assertEqual('10987', result[0])


if __name__ == "__main__":
    unittest.main()
