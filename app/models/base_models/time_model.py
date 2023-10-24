import time


class TimeModel:
    def get_now_timestamp(self):
        """拿到当前时间戳

        Returns:
            int: 当前时间戳
        """
        return int(time.time())
    
    def get_chinese_time(self):

        # 获取当前时间的结构化时间
        current_time = time.localtime()

        # 提取年、月、日
        year = time.strftime("%Y", current_time)
        month = time.strftime("%m", current_time)
        day = time.strftime("%d", current_time)

        return f"{year}{month}{day}"
