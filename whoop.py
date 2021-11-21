from datetime import datetime
from whoop_downloader import whoop_login


class Whoop:

    def __init__(self, ini_path):
        self.client = whoop_login()
        self.client.get_authorization(ini_path)

    def get_hr_data(self, st_time: datetime, end_time: datetime):
        data = []
        for item in self.client.get_hr_timeframe(start=st_time.date().strftime("%Y-%m-%d")):
            dt = datetime.combine(item[0], item[1])
            hr = item[2]
            if st_time <= dt <= end_time:
                data.append((dt, hr))
        return data
