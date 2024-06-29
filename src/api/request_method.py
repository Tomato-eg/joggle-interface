import requests

from src.common.get_yaml import GetYaml
from src.common.log_utils import LogUtils as lu
from src.common.path_utils import PathUtils

log = lu.get_log()
base_file_path = PathUtils().get_project_path()
gy = GetYaml()


class RequestMethod:
    def __init__(self, method, url, data=None, json=None, params=None, headers=None, timeout=None, cookies=None):
        self.method = method
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data
        self.json = json
        self.timeout = timeout
        self.cookies = cookies
        self.session = requests.Session()

    def request_method(self) -> requests.Response:
        try:
            res = self.session.request(
                method=self.method,
                url=self.url,
                headers=self.headers,
                params=self.params,
                data=self.data,
                json=self.json,
                timeout=self.timeout,
                cookies=self.cookies
            )

            return res
        except requests.exceptions.RequestException as e:
            log.info(f'{self.url} + 执行失败,错误原因: + {e}')
            return None

    def request_json(self):
        json_data = self.request_method().json()
        return json_data
