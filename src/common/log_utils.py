import logging
import os
import time

from logging import handlers
# 加载颜色模块
from src.common.path_utils import PathUtils


class LogUtils(object):
    """
        日志级别关系映射
        日志存放的目录
        判断是否存在该路径 判断该路径是否为目录
        日志文件以日期命名
        日志输出格式
        判断是否重复打印日志
    """

    @classmethod
    def get_log(cls):
        log = logging.getLogger(__name__)
        level_relations = {
            'NOTSET': logging.NOTSET,
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }  # 日志级别关系映射

        # 创建日志存放的目录
        project_path = PathUtils().get_project_path()  # 获取根路径
        logs_dir = project_path + "logs"
        # os.path.isdir(logs_dir) 判断该路径是否为目录
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.makedirs(logs_dir)
        # 日志文件以日期命名
        log_file_name = '%s.log' % time.strftime("%Y%m%d", time.localtime())
        # os.path.join(目录, 文件名)
        log_file_path = os.path.join(logs_dir, log_file_name)

        # handlers.TimedRotatingFileHandler()
        rotating_file_handler = handlers.TimedRotatingFileHandler(filename=log_file_path,
                                                                  when='D',  # 按天分隔，一天一个文件
                                                                  interval=30,
                                                                  encoding='utf-8')

        # log_colors_config = {'DEBUG': 'white',
        #                      'INFO': 'cyan',
        #                      'WARNING': 'yellow',
        #                      'ERROR': 'red',
        #                      'CRITICAL': 'bold_red'}

        # 日志输出格式
        # fmt = "%(asctime)s %(levelname)s %(pathname)s %(lineno)d %(message)s"
        # formatter = ColoredFormatter(fmt)
        file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(pathname)s %(lineno)d %(message)s")
        rotating_file_handler.setFormatter(file_formatter)

        # 加上判断，避免重复打印日志
        if not log.handlers:
            # 控制台输出
            console = logging.StreamHandler()
            console.setLevel(level_relations["NOTSET"])
            console.setFormatter(file_formatter)
            # 写入日志文件
            log.addHandler(rotating_file_handler)
            log.addHandler(console)
            log.setLevel(level_relations["DEBUG"])

        return log

    def __del__(self):
        pass


if __name__ == '__main__':
    logger = LogUtils().get_log()
    logger.debug('调试')
    logger.info('信息')
    logger.warning('警告')
    logger.error('报错')
    logger.critical('严重')
