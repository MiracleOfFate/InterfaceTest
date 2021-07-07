from HTMLTestRunner import HTMLTestRunner
import unittest
from datetime import time, datetime
from mail import sendmail


class report:
    def toReport(self):
        dir_path = "../"  # 用于加载测试用例 testchecklist1.py 的路径
        discover = unittest.defaultTestLoader.discover(dir_path, pattern="testchecklist1.py")

        time = datetime.now()
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        report_path = now + "result.html"

        with open(report_path, 'wb')as f:
            runner = HTMLTestRunner(stream=f, verbosity=2, title='接口测试报告', description='用例执行报告')
            runner.run(discover)
        f.close()

        sendmail.sendmail().send_mail(report_path)


if __name__ == '__main__':
    report().toReport()
