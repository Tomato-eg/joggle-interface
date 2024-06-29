import unittest
import socket
from src.common.get_yaml import GetYaml
from src.common.log_utils import LogUtils as lu
from src.common.path_utils import PathUtils
from src.api.request_method import RequestMethod as rm

log = lu.get_log()
base_file_path = PathUtils().get_project_path()
gy = GetYaml()

file_path = base_file_path + 'params\\variable.yaml'
param = gy.read_yaml(file_path)

headers = param['base_set']
base_url = param['base_url']
get = param['method']['GET']
post = param['method']['POST']
put = param['method']['PUT']
delete = param['method']['DELETE']
url_socket = 'www.wanandroid.com'


class PT(unittest.TestCase):

    def setUp(self):
        try:
            self.sock = socket.socket()
            self.sock.connect((url_socket, 80))
            log.info('connected to server')
        except Exception as e:
            log.error(e)
            log.info('connected fail to server')
        pass

    def test_register(self):
        try:
            url = base_url + param['url_path']['register']
            req = rm(post, url, data=param['argument']['register'], headers=headers).request_method()
            data = req.json()
            assert req.status_code == 200
            log.info(data)
            return data['data']['nickname'], data['data']['password']
        except Exception as e:
            log.error(e)

    def test_login(self):
        try:
            url = base_url + param['url_path']['login']
            req = rm(post, url, data=param['argument']['login'], headers=headers).request_method()
            data = req.json()
            assert req.status_code == 200
            log.info(data)
        except Exception as e:
            log.error(e)

    def test_todo(self):
        try:
            url = base_url + '/lg/todo/add/json'
            req = rm(post, url, data=param['argument']['todo'], headers=headers, cookies=param['cookie'],
                     timeout=5).request_method()
            data = req.json()
            assert req.status_code == 200
            # return data['body']['user_id'], data['body']['token']
            log.info(data)
            return data

        except Exception as e:
            log.error(e)

    def tearDown(self):
        try:
            self.sock.close()
        except Exception as e:
            log.error(e)
            log.info('disconnect fail to server')
        pass

