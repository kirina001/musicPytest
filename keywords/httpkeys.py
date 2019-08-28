# -*- coding: UTF-8 -*-
import requests, json, jsonpath, time
from common import logger
import xlwt


class HTTP:
    """
        创建一个http接口请求的关键字类
        data :20190730
    """

    # 构造函数，实例化实例变量
    def __init__(self, writer):
        # 创建session对象，模拟浏览器的cookie管理
        self.session = requests.session()
        # 存放json解析后的结果
        self.jsonres = {}
        # 用来保存所需要的数据，实现关联
        self.params = {}
        # 全局的url
        self.url = ''
        # 写入结果的excel
        self.writer = writer
        # 添加默认UA，模拟chrome浏览器
        self.session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        self.session.headers['Accept'] = 'application/json'

    # 设置地址
    def seturl(self, url):
        url = self.__getparams(url)
        if url.startswith('http'):
            self.url = url
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        else:
            logger.error('error：url地址不合法')
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, 'error：url地址不合法')
            return False

    # 清除头信息
    def clearheader(self):
        logger.info(self.session.headers)
        self.session.headers.clear()
        self.session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        self.session.headers['Accept'] = 'application/json'
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    # 定义login实例方法
    def login(self, path, data=''):
        """
        定义post实例方法，用来发送post请求
        :param path: url路径
        :param data: 键值对传参的字符串
        :return: 无返回值
        """
        try:
            if not path.startswith('http'):
                path = self.url + '/' + path

            # 如果需要传参，就调用post，传递data
            if data == '':
                result = self.session.post(self.url, data=None)
            else:
                # 替换参数
                data = self.__getparams(data)
                # 转为字典
                data = self.__todict(data)
                # 处理带有int表示的value
                isint = 'false'
                for value in data.values():
                    if value.startswith('int'):
                        isint = 'true'
                if isint == 'true':
                    self.__toint(data)
                logger.info('post请求地址' + str(path))
                logger.info('post请求参数' + str(data))

                # 发送请求
                result = self.session.post(path, data=data)

            res = result.text
            logger.info('post返回' + res)

            # print('post返回' + res)
            try:
                res = res[res.find('{'):res.rfind('}') + 1]
            except Exception as e:
                logger.exception(e)

            self.jsonres = json.loads(res)

            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # post请求最多处理带有3层json数据
    def post(self, path, data=''):
        """
        处理数据'area': {'id': '168552091193708544', 'customer': {'id': '168552091042713600'}}
        :param path: rest路径
        :param data: 传入数据
        :return: 成功与否
        """
        try:
            # if not data is None or not data == '':
            if not data == '':
                # 请求中的参数获取{}
                path = self.__getparams(path)
                url = self.url + '/' + path
                logger.info('post请求url:' + url)
                logger.info('post请求data:' + data)

                # 替换参数
                data = self.__getparams(data)
                # 参数组装成dict
                data = self.__todict(data)

                # 处理带有int表示的value
                isint = 'false'
                # 处理file
                isfile = 'false'
                # 处理只有++的数据顺序不可颠倒，因为在该层会删除带有++的key-value
                ismultikeys2 = 'false'
                # 处理只有+的数据
                ismultikeys1 = 'false'
                # 处理songid
                issongid = 'false'

                # 判定是否有特殊数据需要处理
                for key, value in data.items():
                    if value.startswith('int'):
                        isint = 'true'
                    if key.startswith('file'):
                        isfile = 'true'
                    if '++' in key:
                        ismultikeys2 = 'true'
                    if '+' in key:
                        ismultikeys1 = 'true'
                    if key.startswith('songid'):
                        issongid = 'true'

                # 调用对应的处理方法
                if isint == 'true':
                    self.__toint(data)
                if isfile == 'true':
                    data, filelist = self.__tofile(data)
                if ismultikeys2 == 'true':
                    data = self.__handlmultikeys2(data)
                if ismultikeys1 == 'true':
                    data = self.__handlmultikeys1(data)
                if issongid == 'true':
                    data = self.__songid(data)

                logger.info('post处理后的data:' + str(data))

                # 存在文件调用多出一个参数filelist
                if isfile == 'true':
                    # 循环处理多个文件上传
                    for i in range(len(filelist)):
                        result = self.session.post(url=url, data=data, files=filelist[i])
                else:
                    result = self.session.post(url=url, json=data)

                res = result.text
                logger.info('post返回' + res)
                try:
                    res = res[res.find('{'):res.rfind('}') + 1]
                except Exception as e:
                    logger.exception(e)

                self.jsonres = json.loads(res)
                self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
                return True

            else:
                logger.error('data不能为空')
        except Exception as e:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # put接口
    def put(self, path, data):
        '''
        处理数据'author=测试表演&name=AlienBo.mp3&speed=0&style+Id=2'
        :param path: rest路径
        :param data: 传入数据
        :return: 成功与否
        '''
        try:
            if not data == '':
                path = self.__getparams(path)
                url = self.url + '/' + path
                logger.info('putplay请求url:' + url)
                logger.info('putpaly请求data:' + data)

                # 替换参数
                data = self.__getparams(data)
                # 参数组装成dict
                data = self.__todict(data)

                # 处理带有int表示的value
                isint = 'false'
                # 处理只有++的数据顺序不可颠倒，因为在该层会删除带有++的key-value
                ismultikeys2 = 'false'
                # 处理只有+的数据
                ismultikeys1 = 'false'
                # 处理songid
                issongid = 'false'
                # 处理channelid
                ischannelid = 'false'
                # 判定是否有特殊数据需要处理
                for key, value in data.items():
                    if value.startswith('int'):
                        isint = 'true'
                    if '++' in key:
                        ismultikeys2 = 'true'
                    if '+' in key:
                        ismultikeys1 = 'true'
                    if key.startswith('songid'):
                        issongid = 'true'
                    if key.startswith('channelid'):
                        ischannelid = 'true'

                # 调用对应的处理方法
                if isint == 'true':
                    self.__toint(data)
                if ismultikeys2 == 'true':
                    data = self.__handlmultikeys2(data)
                if ismultikeys1 == 'true':
                    data = self.__handlmultikeys1(data)
                if issongid == 'true':
                    data = self.__songid(data)
                if ischannelid == 'true':
                    data = self.__channelid(data)

                logger.info('put处理后的data：' + str(data))

                # 发送请求
                result = self.session.put(url=url, json=data)
                res = result.text
                logger.info('putplay返回' + res)
                try:
                    res = res[res.find('{'):res.rfind('}') + 1]
                except Exception as e:
                    logger.exception(e)

                self.jsonres = json.loads(res)
                self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
                return True

            else:
                logger.error('data不能为空')
        except Exception as e:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # get 请求支持restful
    def get(self, path, data=''):
        """
        支持普通的get请求也支持restful风格的get请求
        :param path: rest路径
        :param data: 请求数据
        :return: 成功与否
        """
        try:
            if not path.startswith('http'):
                # 处理url带有{}
                path = self.__getparams(path)
                path = self.url + '/' + path
                logger.info('get请求url:' + str(path))
            # 参数为空的请求
            if data == '':
                result = self.session.get(path)
            else:
                # 替换参数
                data = self.__getparams(data)
                p = data.split('=')
                path = path + '/' + p[1]
                logger.info('rest风格get请求' + str(path))
                result = self.session.get(path)

            res = result.text
            logger.info('get返回' + result.text)
            try:
                res = res[res.find('{'):res.rfind('}') + 1]
            except Exception as e:
                logger.exception(e)

            self.jsonres = json.loads(res)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # 播放曲目
    def play(self, path, data):
        """
        播放曲目接口
        :param path: url接口参数
        :param data: 请求数据
        :return: 成功与否
        """
        try:
            if not path.startswith('http'):
                path = self.url + '/' + path
                logger.info('play请求url:' + str(path))
            # 如果需要传参，就调用post，传递data
            if data == '':
                result = self.session.get(path)
            else:
                # 替换参数
                data = self.__getparams(data)
                # restful风格请求
                path = path + '/' + str(data)
                # print('处理后的请求'+path)
                logger.info('play请求' + path)
                res = self.session.get(path)

            # 返回结果处理
            # 时间戳
            timestamp = int(round(time.time() * 1000))
            if str(res.status_code) == '200':

                res = {"message": "播放成功", "code": 0, "timestamp": timestamp}
                logger.info('play返回结果' + str(res))

                self.jsonres = res
                self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
                return True
            else:
                res = {"message": "播放失败", "code": -1, "timestamp": timestamp}
                logger.info('play返回结果' + str(res))

                self.jsonres = res
                self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
                return False

        except Exception as e:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # 下载曲目
    def download(self, path, data):
        """
        下载曲目保存到指定位置 filename = './lib/music_download/test_down.mp3'
        :param path: 接口名称
        :param data: 请求数据
        :return: 成功与否
        """
        try:
            if not path is None:
                data = self.__getparams(data)
                url = self.url + '/' + path + '/' + data

                result = self.session.get(url=url, stream=True)
                # logger.info('download请求返回状态：' + str(result.status_code))

                # 处理服务器返回的数据
                filename = './lib/music_download/test_down.mp3'
                # 将文件保存到指定位置
                with open(filename, "wb") as f:
                    for chunk in result.iter_content(chunk_size=512):
                        f.write(chunk)
                # 时间戳
                timestamp = int(round(time.time() * 1000))
                if str(result.status_code) == '201':

                    result = {"message": "下载成功", "code": 0, "timestamp": timestamp, "downloadpath": filename}
                    logger.info('download请求返' + str(result))
                    self.jsonres = result

                    self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                    self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
                    return True
                else:
                    result = {"message": "下载失败", "code": 0, "timestamp": timestamp}
                    logger.info('download请求返' + str(result))
                    self.jsonres = result

                    self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
                    self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
                    return False

            else:
                logger.info('请求方法url参数有误')

        except Exception as e:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(result))
            logger.exception(e)
            return False

    # 删除json
    def deletejson(self, data):
        """
        删除接口，待删除的数据添加在请求体中
        :param data: 请求数据
        :return: 成功与否
        """
        try:
            if not data is None or not data == '':
                url = self.url
                logger.info('deletejson请求url:' + url)

                # 替换参数
                data = self.__getparams(data)
                # 参数分割 支持删除多首曲目
                data = data.split(',')
                # 发请请求
                result = self.session.delete(url=url, json=data)
                res = result.text
                logger.info('deletejson返回' + res)
                try:
                    res = res[res.find('{'):res.rfind('}') + 1]
                except Exception as e:
                    logger.exception(e)

                self.jsonres = json.loads(res)
                self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
                return True
            else:
                logger.error('data不能为空')
        except Exception as  e:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # 删除restful
    def deleterest(self, data):
        """
        删除接口 待删除的数据添加在url后面restful风格
        :param data:请求数据
        :return:成功与否
        """
        try:
            if not data is None or not data == '':
                url = self.url
                # 替换参数
                data = self.__getparams(data)
                url = url + '/' + str(data)
                logger.info('deleterest请求url:' + url)

                result = self.session.delete(url)
                res = result.text
                logger.info('deleterest返回' + res)
                try:
                    res = res[res.find('{'):res.rfind('}') + 1]
                except Exception as e:
                    logger.exception(e)

                self.jsonres = json.loads(res)
                self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
                return True
            else:
                logger.error('data不能为空')
        except Exception as e:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.exception(e)
            return False

    # 断言相等
    def assertequals(self, jsonpaths, value):
        """
        定义断言相等的关键字，用来判断json的key对应的值和期望值相等
        :param jsonpaths: 通过jsonpath获取返回的数据
        :param value: 期望结果
        :return:
        """
        res = 'None'
        try:
            res = str(jsonpath.jsonpath(self.jsonres, jsonpaths)[0])
        except Exception as e:
            logger.exception(e)

        value = self.__getparams(value)

        if res == str(value):
            logger.info('测试通过')
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
            return 'Pass'
        else:
            logger.info('测试失败')
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
            return False

    # 实现关联
    def savejsons(self, jsonpaths, param):
        '''
        实现关联 通过jsonpath获取返回参数，保存到变量中{}
        :param jsonpath: 通过jsonpath获取返回的数据
        :param param: 保存参数名称
        :return:
        '''
        res = 'None'
        try:
            res = str(jsonpath.jsonpath(self.jsonres, jsonpaths)[0])
        except Exception as e:
            logger.exception(e)

        self.params[param] = res
        if res is not 'None':

            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
            return True
        else:
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(res))
            return False

    # 自定义参数保存
    def savevalue(self, value, param):
        """
        自定义参数保存
        :param value: 需要保存的参数值
        :param param: 参数名称
        :return: 是否保存成功
        """
        try:
            self.params[param] = value
        except Exception as e:
            logger.exception(e)

        if value != '':
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, value)
            return True
        else:
            value = 'None'
            self.writer.writefalse(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, value)
            return False

    # 给头添加一个键值对的关键字
    def addheader(self, key, value):
        """
        给头添加一个键值对的关键字
        :param key: 需要添加的key
        :param value: 添加的value
        :return: 成功与否
        """
        value = self.__getparams(value)
        self.session.headers[key] = value
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, str(value))
        return True

    # 从头里面删除一个键值对
    def removeheader(self, key):
        self.session.headers.pop(key)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, str(key))
        return True

    # 替换参数
    def __getparams(self, s):
        """
        替换参数值
        :param s: 传入参数{a}
        :return: 解析后的参数值a=1111
        """
        # logger.info('参数化列表:' + str(self.params))
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s

    # 请求参数转换为dict
    def __todict(self, s):
        """
        将一个标准的URL地址参数转换为一个dict
        :param s: 需要转换的数据 username=Tester55&password=123456&ttt=ccccc
        :return: 转换后的dict  {'username':'Tester55','password':'123456','tttt':'ccccc'}
        """
        httpparam = {}
        # 分割参数个数
        param = s.split('&')
        for ss in param:
            # 把键值对分开
            p = ss.split('=')
            if len(p) > 1:
                httpparam[p[0]] = p[1]
            else:
                httpparam[p[0]] = ''

        return httpparam

    # 处理需要转换类型的value
    def __toint(self, data):
        """
        处理需要转换类型的value
        :param data: 传入data
        :return: value中带有int的数据替换后的dict
        """
        # 遍历传入的data中的value是否包含int需要转换
        for key, value in data.items():
            if 'int' in value:
                tmp = value.split('int')
                value = int(tmp[1])
                data[key] = value
        return data

    # 文件处理
    def __tofile(self, data):
        """
        上传文件时需要的参数列表
        :param data: 传入data
        :return: 处理后的data和files参数
        """
        datatemp = {}
        files = {}
        filelist = []

        for key, value in data.items():
            # file文件以外的参数单独处理
            if value.find('.') < 0:
                datatemp[key] = value
                data = datatemp
            else:
                files[key] = open(value, 'rb')
                files['file'] = files.pop(key)
                filelist.append(files)
                files = {}

        return data, filelist

    # 处理多层key ++
    def __handlmultikeys2(self, data):

        add = {}
        # 原始需要处理的key ++
        keylist = []
        # 需要存储的值
        valuelist = []
        # 需要删除的key
        removekey = []

        for key, value in data.items():
            if '++' in key:
                removekey.append(key)
                keylist.append(key)
                valuelist.append(value)

        # 处理第一层key
        keyname = []
        addname = []
        for i in range(len(keylist)):
            if '++' in keylist[i]:
                tmp = keylist[i].split('++')
                keyname.append(tmp[0])
                addname.append(tmp[1])

        # 判定是否有重复数据
        for i in range(len([keyname])):
            if keyname[i] == keyname[i + 1]:
                # print('只有一个key')
                newkeyname = keyname[0]
            else:
                print('其他处理方式')
        # 处理第一层key和value
        newkey = {}
        for i in range(len(addname)):
            newkey[addname[i]] = valuelist[i]

        # 处理最外层key
        dataadd = {}
        dataadd[newkeyname] = newkey
        # 拼接最后的data
        data.update(dataadd)

        # 删除原始data中的带有+的key
        for i in range(len(removekey)):
            data.pop(removekey[i])
        return data

    # 处理带有一个+的数据
    def __handlmultikeys1(self, data):
        """
        处理带有一个+的数据
        :param data:原始数据
        :return:返回拼接后的完整数据 例如：{'name': '新增区域', 'customer': {'id': '169237559774285824'}}
        """
        # 寻找需要处理的+ 可能存在1个也可能存在多个需要处理的+ 应该灵活适配
        keylist = []
        valuelist = []
        removekey = []
        for key, value in data.items():
            if '+' in key:
                removekey.append(key)
                keylist.append(key)
                valuelist.append(value)

        # 处理key与value对应
        addname = {}
        addvalue = {}
        for i in range(len(keylist)):
            if '+' in keylist[i]:
                tmp = keylist[i].split('+')
                addname[tmp[0]] = {}
                addvalue[tmp[1]] = valuelist[i]
                addname[tmp[0]] = addvalue
                addvalue = {}
        # 将处理后的数据加入原始data
        data.update(addname)

        # 删除原始data中的带有+的key
        for i in range(len(removekey)):
            data.pop(removekey[i])

        return data

    # 处理上传曲目的songid
    def __songid(self, data):
        """
        处理上传曲目的songid
        :param data: 传入含有sognid的data
        :return: 返回处理后的songid
        """
        # 处理传入的sognid
        songid = []
        for key in data:
            if key.startswith('songid'):
                songid.append(data[key])
        # 删除多余的key
        if songid:
            kelist = []
            for x in data.keys():
                if x.startswith('songid'):
                    kelist.append(x)
            for x in kelist:
                data.pop(x)

            # 将处理好的songid传入songList
            sognlist = []
            tmp = {}
            # songid存入songlist
            for i in range(len(songid)):
                tmp['id'] = songid[i]
                sognlist.append(tmp)
                tmp = {}
            data['songList'] = sognlist
        return data

    # 处理解除绑定频道的channelid
    def __channelid(self, data):
        """
        处理上传曲目的songid
        :param data: 传入含有channelid的data
        :return: 返回处理后的channelid
        """
        # 处理传入的channelid
        channelid = []
        for key in data:
            if key.startswith('channelid'):
                channelid.append(data[key])
        return channelid
