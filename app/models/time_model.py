import time


class TimeModel:
    def get_now_timestamp(self):
        """拿到当前时间戳

        Returns:
            int: 当前时间戳
        """
        return int(time.time())
