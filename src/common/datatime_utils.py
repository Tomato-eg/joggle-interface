import time
import traceback

from src.common.log_utils import LogUtils


class DatatimeUtils:
    def __init__(self):
        self.logger = LogUtils().get_log()

    def get_now_datetime(self):
        try:
            now_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            return now_datetime
        except Exception as e:
            # traceback.format_exc()
            self.logger.error(traceback.format_exc())
            self.logger.error("获取时间失败：" + str(e))


if __name__ == '__main__':
    print(DatatimeUtils().get_now_datetime())
