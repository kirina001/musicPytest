import unittest,datetime,time
from parameterized import parameterized
from keywords.webkeys import Web
from keywords.appkeys import APP
from keywords.soapkeys import SOAP
from keywords.httpkeys2 import HTTP
from myunittest import datadriven


class TestWeb(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = None
        if datadriven.runtype == 'WEB':
            cls.obj = Web(datadriven.writer)

        if datadriven.runtype == 'APP':
            cls.obj = APP(datadriven.writer)

        if datadriven.runtype == 'HTTP':
            cls.obj = HTTP(datadriven.writer)

        if datadriven.runtype == 'SOAP':
            cls.obj = SOAP(datadriven.writer)

    @parameterized.expand(datadriven.alllist)
    def test_http(self, index, name, key, param1, param2, param3):
        """"""
        # print(name)
        # 标识是否运行
        flg = False
        try:
            index = int(index)
            # 设置当前执行写入的行数
            datadriven.writer.row = index
            # print(index)
            # 如果不是sheet就运行
            flg = True
        except:
            # 如果是sheet，就切换写入的sheet页面，不执行
            datadriven.writer.set_sheet(index)

        # 如果需要运行用例
        if flg:
            line = [key, param1, param2, param3]
            # print(line)
            func = datadriven.geffunc(line, self.obj)
            # print(func)
            lenargs = datadriven.getargs(func)
            # 反射执行
            res = datadriven.run(func, lenargs, line)

            res =str(res)
            self.__eqult(res)


            # self.assertEqual(self,res, 'Pass')

            print(res)
            return res
            # if res is False:
            #     self.fail('关键字执行失败')


    # def test_add(self,res):
    #     self.assertNotEqual(self, res, 'Pass', msg=None)
    #     # """"""
    #     # self.assertEqual(ttt.add(x, y), z)
    #     # self.assertEquals()

    def __eqult(self,res):
        self.assertEqual(self,res,'Pass')