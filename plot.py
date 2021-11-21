import whoop
import wahoo
import argparse
import plotly.graph_objects as go
from datetime import datetime


def string_to_datetime(s):
    return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fit_file', help='Path to Wahoo .fit file ')
    parser.add_argument('whoop_cred_file', help='Path to whoop.ini file')
    parser.add_argument('st_time', type=string_to_datetime, help='Start time format: YYYY-MM-DD HH:MM:SS')
    parser.add_argument('end_time', type=string_to_datetime, help='End time format: YYYY-MM-DD HH:MM:SS')

    args = parser.parse_args()

    fig = go.Figure()
    for client, name in [(wahoo.Wahoo(fitfile_path=args.fit_file), 'Wahoo'),
                         (whoop.Whoop(ini_path=args.whoop_cred_file), 'Whoop')]:
        x = []
        y = []
        for item in client.get_hr_data(st_time=args.st_time, end_time=args.end_time):
            x.append(item[0])
            y.append(item[1])
        fig.add_trace(go.Scatter(x=x, y=y, name=name))

    fig.show()
