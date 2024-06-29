import random
import string

from src.common.log_utils import LogUtils
from src.common.path_utils import PathUtils

# 日志打印
logger = LogUtils.get_log()
# 根目录
base_path = PathUtils().get_project_path()


class OrderRand:

    def order_generate(self):
        # 固定的前缀
        prefix = '2024051819'

        # 生成随机数字部分（不包括末两位字母）
        # 这里假设随机数字部分长度为10（因为总长度减去前缀和末两位字母的长度）
        random_digits = ''.join(random.choices('0123456789', k=20))

        # 生成随机字母部分（末两位）
        random_letters = ''.join(random.choices(string.ascii_letters, k=2))

        # 拼接字符串
        result = prefix + random_digits + random_letters

        logger.info(result)
        return result



