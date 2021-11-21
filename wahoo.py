import fitparse
from datetime import datetime


class Wahoo:

    def __init__(self, fitfile_path):
        self.fitfile = fitparse.FitFile(fitfile_path)

    def get_hr_data(self, st_time: datetime, end_time: datetime):
        data = []
        for record in self.fitfile.get_messages():
            values = record.get_values()
            if 'heart_rate' in values:
                dt = values['timestamp']
                hr = values['heart_rate']
                if st_time <= dt <= end_time:
                    data.append((dt, hr))
        return data
