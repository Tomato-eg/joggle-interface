import random
from datetime import datetime


class DateTimeRand:
    def get_time(self):
        hour = str(random.randint(0, 23)).zfill(2)  # 生成0-23的小时，并确保是两位数  
        minute = str(random.randint(0, 59)).zfill(2)  # 生成0-59的分钟，并确保是两位数  
        second = str(random.randint(0, 59)).zfill(2)  # 生成0-59的秒数，并确保是两位数  

        date_time = datetime(2024, 5, 19, int(hour), int(minute), int(second))
        return date_time


if __name__ == '__main__':
    x = DateTimeRand().get_time()
    print(x)