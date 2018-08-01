# -*-coding:utf-8-*-
import sys, os

reload (sys)
sys.setdefaultencoding ('utf-8')
sys.path.append (os.path.abspath ('../..'))
from app import util
from app.mytest import Myunittest
from app.testcase import Testcase
import unittest
from config.configure import Config


'''
===========说明============
功能:测试用例定义
入口:ecxel表格测试用例
==========================
'''

# Myunittest,
class ScheduleCompany (Myunittest):
    """客户端:搜索测试"""

    @classmethod
    def setUpClass(cls):
        super (ScheduleCompany,cls).setUpClass (appPakage='com.yonyou.buyer')

    testcaseList = util.getXlsTestCase ('search')
    for testcase in testcaseList:
        # 判断测试用例是否执行 1——执行,0——不执行;
        exec (util.FUNC_TEMPLATE.format (func=testcase['case_id'],
                                         casename=testcase['case_name'],
                                         onecase=testcase,
                                         sheetname='search',
                                         state=testcase['state']
                                         ))


if __name__ == '__main__':
    unittest.main ()
